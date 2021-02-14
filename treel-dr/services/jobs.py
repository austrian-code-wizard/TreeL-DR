from services.gpt3 import GPT3Service
from services.twilio import TwilioService
from services.outlook import OutlookService
from services.user import UserService
from datetime import datetime, timedelta
from schemas.user import UserSchema
from logging import Logger, getLogger, DEBUG, root
import pytz
import coloredlogs
from config import LOG_LEVEL

class JobService:
    def __init__(self, twilio_service: TwilioService, user_service: UserService, gpt3_service: GPT3Service, outlook_service: OutlookService, logger: Logger = None):
        root.setLevel(DEBUG)
        if not logger:
            logger = getLogger("JobServiceLogger")
        coloredlogs.install(level=LOG_LEVEL, logger=logger)
        self._logger = logger
        self._logger.setLevel(DEBUG)
        self._twilio_service = twilio_service
        self._user_service = user_service
        self._gpt3_service = gpt3_service
        self._outlook_service = outlook_service

    def process_user_emails(self, user: UserSchema, token: str, ignore_lastJob=False):
        self._logger.debug(f"Getting emails")
        if not ignore_lastJob:
            start = max((datetime.utcnow() - timedelta(hours=user.interval)).replace(tzinfo=pytz.UTC), user.lastJob)
        else:
            start = datetime.utcnow() - timedelta(hours=user.interval)
        emails = self._outlook_service.get_emails(token, start=start)
        self._logger.debug(f"Got emails")
        parsed_emails = []
        for email in emails:
            email["attributes"] = self._gpt3_service.get_email_attributes(email["text"])
            self._logger.debug(f"Parsed email {email['subject']}")
            if email["attributes"]["category"] in user.subscribed:
                parsed_emails.append(email)
        self._logger.debug(f"Parsed all emails")
        if len(parsed_emails) == 0:
            self._twilio_service.send_no_emails_found(user)
            self._logger.debug(f"Sent no email found text")
        else:
            self._logger.debug(f"Sending header")
            self._twilio_service.send_treeldr_header(user, len(parsed_emails))
            for i, email in enumerate(parsed_emails):
                self._twilio_service.send_treeldr(user, email, len(parsed_emails), i+1)
                self._logger.debug(f"Sent email text {email['subject']}")
            self._twilio_service.send_treeldr_footer(user)
        self._logger.debug(f"Sent all texts")
        user_update = UserSchema(**{
            "lastJob": datetime.utcnow(),
            "nextJob": datetime.utcnow() + timedelta(hours=user.interval)
        })
        self._user_service.updateUser(user_update, user.email)
        self._logger.debug("done!")
        return len(parsed_emails)