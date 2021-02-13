import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from config import SERVICE_ACCOUNT_PATH

def load_db():
    # Firebase access
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)
    return firestore.client()
