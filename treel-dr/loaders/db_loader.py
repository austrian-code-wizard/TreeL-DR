import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from config import SERVICE_ACCOUNT_PATH, PROJECT_ID

def load_db():
    # Firebase access
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)
    except FileNotFoundError:
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
        'projectId': PROJECT_ID,
        })
    return firestore.client()
