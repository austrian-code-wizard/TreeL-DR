import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# 
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTHORITY = "https://login.microsoftonline.com/common"
REDIRECT_PATH = "/getAToken"
APP_URL = "https://treel-dr.wl.r.appspot.com"
PORT = int(os.getenv("PORT"))
SCOPE = ["User.ReadBasic.All", "Mail.Read"]

SERVICE_ACCOUNT_PATH = os.getenv("SERVICE_ACCOUNT_PATH")

#### GPT3 / OPEN AI CONFIG ####

OPENAI_KEY = os.getenv("OPENAI_KEY")

#### TWILIO CONFIG ####

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = "+14804854257"

CONFIRMATION_PAGE_URL = "https://email-project-d4353e.webflow.io/confirmation"
LOG_LEVEL = "DEBUG"

SESSION_TYPE = "redis"
SECRET_KEY = os.getenv("SECRET_KEY")

PROJECT_ID = "treel-dr"

REDIS_KEY = os.getenv("REDIS_KEY")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))

#### CHECKBOOK CONFIG ####

CHECKBOOK_CHECK_ENPOINT = 'https://api.sandbox.checkbook.io/v3/check/digital'