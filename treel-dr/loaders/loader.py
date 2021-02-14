from loaders.app_loader import load_app
from loaders.session_loader import load_session
from loaders.db_loader import load_db
from loaders.redis_loader import load_redis
from services.auth import AuthService
from services.user import UserService
from services.outlook import OutlookService
from services.twilio import TwilioService
from services.gpt3 import GPT3Service
from services.jobs import JobService

def load():
    app = load_app()
    app = load_redis(app)
    session = load_session(app)
    db = load_db()
    auth_service = AuthService(session)
    user_service = UserService(db)
    outlook_service = OutlookService()
    twilio_service = TwilioService()
    gpt3_service = GPT3Service()
    job_service = JobService(twilio_service, user_service, gpt3_service, outlook_service)
    return {
        "app": app,
        "session": session,
        "auth_service": auth_service,
        "user_service": user_service,
        "outlook_service": outlook_service,
        "twilio_service": twilio_service,
        "gpt3_service": gpt3_service,
        "job_service": job_service
    }