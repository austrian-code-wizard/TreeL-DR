from twilio.rest import Client
from logging import Logger, getLogger
from schemas.user import UserSchema
from typing import Dict
from config import TWILIO_AUTH_TOKEN, TWILIO_NUMBER, TWILIO_SID, LOG_LEVEL
from utils import format_event_name
import coloredlogs

class TwilioService:
    def __init__(self, logger: Logger = None):
        if not logger:
            logger = getLogger("TwilioServiceLogger")
        coloredlogs.install(level=LOG_LEVEL, logger=logger)
        self._logger = logger
        self._client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_text(self, phone_number: str, text: str):
        message = self._client.messages.create(
                        body=text,
                        from_=TWILIO_NUMBER,
                        to=phone_number
                    )
        return True

    def send_treeldr_header(self, user: UserSchema, num_emails: int):
        text = f"\n\n🌲Your TreeL;DR🌲\n\nHi {user.first},\nWe found {num_emails} new emails for the categories you're subscribed to 📧. Here you go:"
        self.send_text(user.phone_number, text)

    def send_treeldr_footer(self, user: UserSchema):
        text = f"That was your TreeL;DR 🌈. But don't worry! You will receive your next one in {user.interval} hours 🚀."
        self.send_text(user.phone_number, text)

    def send_treeldr(self, user: UserSchema, email_info: Dict, num_emails: int, email_index: int):
        text = f'\n\n📧{email_index}/{num_emails}📧\n\nCategory: {format_event_name(email_info["attributes"]["category"])}\nSender: {email_info["from"]}\nSummary: {email_info["attributes"]["summary"]}\nAction Needed: {email_info["attributes"]["action_needed"] if email_info["attributes"]["action_needed"] != "" else "None"}\nDeadline: {email_info["attributes"]["deadline"] if email_info["attributes"]["deadline"] != "" else "None"}'
        self.send_text(user.phone_number, text)

    def send_no_emails_found(self, user: UserSchema):
        text = f"\n\n🌲Your TreeL;DR🌲\n\nHi {user.first},\nYou did not receive any new emails in the categories you are subscribed to. But don't worry! You will receive your next one in {user.interval} hours 🚀."
        self.send_text(user.phone_number, text)

    def send_welcome(self, user: UserSchema):
        text = f"\n\n🌲Welcome to TreeL;DR🌲\n\nWe will send your email digest every {user.interval} hours.\nYou are currently subscribed to emails about {(', '.join([format_event_name(event_type) for event_type in user.subscribed]))}."
        self.send_text(user.phone_number, text)