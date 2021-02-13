import uuid
import requests
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_session import Session  # https://pythonhosted.org/Flask-Session
from services.user import UserService
from services.outlook import OutlookService
from services.auth import AuthService
from loaders.loader import load
from config import REDIRECT_PATH

dependencies = load()
app = dependencies["app"]

@app.route("/login")
def login():
    auth_service = dependencies["auth_service"]
    # Technically we could use empty list [] as scopes to do just sign in,
    # here we choose to also collect end user consent upfront
    auth_uri = auth_service.build_auth_code_flow()
    return redirect(auth_uri)

@app.route(REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    try:
        auth_service = dependencies["auth_service"]
        user_service = dependencies["user_service"]
        outlook_service = dependencies["outlook_service"]

        token = auth_service.get_access_token(request.args)

        user = outlook_service.get_user_info(token)

        cache = auth_service.load_cache()

        user.token = auth_service.dumps_cache(cache)

        res = user_service.upsertUser(user)

        return jsonify({"info": "Success!"})
    except ValueError as e:  # Usually caused by CSRF
        return jsonify({"error": {e}})

@app.route("/graphcall/<string:email>")
def graphcall(email):
    auth_service = dependencies["auth_service"]
    user_service = dependencies["user_service"]
    outlook_service = dependencies["outlook_service"]

    user = user_service.getUser(email)
    token = auth_service.get_access_token_from_serialized(user.token)
    emails = outlook_service.get_emails(token)
    return jsonify(emails)

if __name__ == "__main__":
    app.run()

