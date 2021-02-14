import requests

class CheckbookService:
    default_nonprofit = 'nonprofit2'
    default_user_email = 'moritz.stephan2@outlook.com'
    default_donation_amount = 25

    CHECKBOOK_CHECK_ENPOINT = 'https://api.sandbox.checkbook.io/v3/check/digital'

    def __init__(self, user_service):
        self.user_service = user_service

    def donate(self, email, nonprofit, routing_num, account_num, amount, message):
        try:
            # nonprofit exists
            nonprofit = self.user_service.getUser(nonprofit)
        except Exception as e:
            # nonprofit doesnt exist -> use default
            nonprofit = self.user_service.getUser(self.default_nonprofit)

        try:
            # user exists
            user = self.user_service.getUser(email)
        except Exception as e:
            # user doesnt exist -> use default
            user = self.user_service.getUser(self.default_user_email)

        auth = user.cb_p_key + ':' + user.cb_s_key
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": auth
        }
        data = {
            "recipient": nonprofit.email,
            "name": nonprofit.first,
            "amount": amount,
            "description": f"Donation from {user.first} {user.last} via TreeLDR - {message if message else 'thanks'}"
        }

        r = requests.post(self.CHECKBOOK_CHECK_ENPOINT, headers=headers, json=data)
        r.raise_for_status()