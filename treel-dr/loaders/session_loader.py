from flask import session
from flask_session import Session

def load_session(app):
    Session(app)
    return session