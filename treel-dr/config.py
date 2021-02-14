import os

CLIENT_ID = "0df7c0e4-a959-4920-8069-6f2e71f990f1" # Application (client) ID of app registration

CLIENT_SECRET = "PB.E9AYQBWKw5_Y~3M-_5UL4yz8CXc-DQt" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

APP_URL = "http://localhost:8000"

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = "https://graph.microsoft.com/v1.0/me/mailFolders('Inbox')/messages"  # This resource requires no admin consent ?$filter=ReceivedDateTime ge 2021-02-13T07:45:43Z and receivedDateTime lt 2021-02-13T09:25:43Z

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All", "Mail.Read"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session

SERVICE_ACCOUNT_PATH = '/Users/moritzstephan/Downloads/treel-dr-82e7451bd561.json'

#### GPT3 / OPEN AI CONFIG ####

OPENAI_KEY = os.environ.get("OPENAI_API_KEY", None)

#### TWILIO CONFIG ####

TWILIO_SID = "ACc13653cd13572fb1dea854e3fda15a84"

TWILIO_AUTH_TOKEN = "a78820a53ba80154b97c3f8c7ed4f2aa"

TWILIO_NUMBER = "+14804854257"

CONFIRMATION_PAGE_URL = "https://email-project-d4353e.webflow.io/confirmation"

