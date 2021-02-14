import uuid
import requests
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_session import Session  # https://pythonhosted.org/Flask-Session
from services.user import UserService
from services.outlook import OutlookService
from services.auth import AuthService
from loaders.loader import load
from config import REDIRECT_PATH, CONFIRMATION_PAGE_URL, LOG_LEVEL, PORT
from schemas.user import UserSchema
from utils import remove_none_from_dict, clean_phone_number, handle_error
from datetime import datetime, timedelta
import pytz
import coloredlogs

dependencies = load()
app = dependencies["app"]
logger = app.logger

coloredlogs.install(level=LOG_LEVEL, logger=logger)

@app.route("/login", methods=["POST"])
@handle_error
def login():
    auth_service = dependencies["auth_service"]
    session = dependencies["session"]
    # Technically we could use empty list [] as scopes to do just sign in,
    # here we choose to also collect end user consent upfront
    auth_uri = auth_service.build_auth_code_flow()
    user = UserSchema(**{
        "first": request.form["first_name"],
        "last": request.form["last_name"],
        "interval": int(request.form["interval"]),
        "phone_number": clean_phone_number(request.form["phoneOne"]),
        "lastJob": datetime.utcnow() - timedelta(hours=24 * 365),
        "subscribed": [key for key in ["covid_updates", "job_opportunities", "school", "events"] if key in request.form]
    })
    session["user_info"] = remove_none_from_dict(user.dict())
    return redirect(auth_uri)

@app.route(REDIRECT_PATH)  # Its absolute URL must match your app's redirect_uri set in AAD
@handle_error
def authorized():
    auth_service = dependencies["auth_service"]
    user_service = dependencies["user_service"]
    outlook_service = dependencies["outlook_service"]
    twilio_service = dependencies["twilio_service"]
    session = dependencies["session"]

    token = auth_service.get_access_token(request.args)

    user = outlook_service.get_user_info(token)
    user = user.dict()
    user.update(session["user_info"])
    user = UserSchema(**user)

    cache = auth_service.load_cache()

    user.token = auth_service.dumps_cache(cache)
    user.nextJob = datetime.utcnow() + timedelta(hours=user.interval)

    res = user_service.upsertUser(user)

    twilio_service.send_welcome(user)
    session.clear()
    return redirect(CONFIRMATION_PAGE_URL)

@app.route("/sync")
@handle_error
def sync():
    auth_service = dependencies["auth_service"]
    user_service = dependencies["user_service"]
    job_service = dependencies["job_service"]

    users = user_service.getUsersToProcess()
    logger.debug("Got users")
    result = []
    for user in users:
        token = auth_service.get_access_token_from_serialized(user.token)
        logger.debug("Processing emails")
        num_emails = job_service.process_user_emails(user, token)
        logger.debug("Got emails")
        cache = auth_service.load_cache()
        user_update = UserSchema(**{
            "token": auth_service.dumps_cache(cache)
        })
        user_service.updateUser(user_update, user.email)
        result.append({user.email: num_emails})
    return jsonify(result)

@app.route("/syncnow/<string:email>")
@handle_error
def sync_now(email: str):
    auth_service = dependencies["auth_service"]
    user_service = dependencies["user_service"]
    job_service = dependencies["job_service"]

    user = user_service.getUser(email)
    token = auth_service.get_access_token_from_serialized(user.token)
    num_emails = job_service.process_user_emails(user, token, ignore_lastJob=True, process_descending=True)
    cache = auth_service.load_cache()
    user_update = UserSchema(**{
        "token": auth_service.dumps_cache(cache)
    })
    user_service.updateUser(user_update, user.email)
    return jsonify({user.email: num_emails})

@app.route("/donate", methods=["POST"])
@handle_error
def donate():
    email = request.form['email']
    nonprofit = request.form['nonprofit']
    routing_num = request.form.get('routing_num', '')
    account_num = request.form.get('account_num', '')
    amount = int(request.form.get('amount', 0))
    message = request.form.get('message', '')

    checkbook_service = dependencies['checkbook_service']
    redirect_url = checkbook_service.donate(email, nonprofit, routing_num, account_num, amount, message)

    return redirect(redirect_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)

