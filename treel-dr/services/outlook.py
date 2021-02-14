from logging import Logger, getLogger
from schemas.user import UserSchema
from datetime import datetime
import requests
from bs4 import BeautifulSoup

class OutlookService:
    def __init__(self, logger: Logger = None):
        self._ENDPOINTS = {
            "GET_EMAILS": "https://graph.microsoft.com/v1.0/me/mailFolders('Inbox')/messages",
            "GET_USER": "https://graph.microsoft.com/v1.0/me?$select=givenName,surname,mail,userPrincipalName"
        }
        if not logger:
            logger = getLogger("OutlookServiceLogger")
        self._logger = logger

    def _graphql_request(self, endpoint: str, token: str):
        return requests.get(endpoint, headers={'Authorization': 'Bearer ' + token}).json()

    def get_emails(self, token, start: datetime = None, end: datetime = None):
        url = self._ENDPOINTS["GET_EMAILS"]
        if start or end:
            url += "?$filter="
        if start:
            url += f"ReceivedDateTime ge {start.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        if end:
            if start:
                url += " and"
            url += f" receivedDateTime lt {end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        graph_data = self._graphql_request(url, token)

        results = []
        for result in graph_data["value"]:
            soup = BeautifulSoup(result["body"]["content"], features="html.parser")

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out

            # get text
            text = soup.get_text()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk).replace("\u00a0", " ")
            results.append({
                "from": result["from"]["emailAddress"]["address"],
                "subject": result["subject"],
                "text": text,
                "link": result["webLink"]
            })
        return results

    def get_user_info(self, token: str):
        response = self._graphql_request(self._ENDPOINTS["GET_USER"], token)
        user_info_dict = {
            'email': response["userPrincipalName"]
        }
        return UserSchema(**user_info_dict)