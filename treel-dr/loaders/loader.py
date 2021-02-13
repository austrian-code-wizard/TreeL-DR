from loaders.app_loader import load_app
from loaders.session_loader import load_session
from loaders.db_loader import load_db
from services.auth import AuthService
from services.user import UserService
from services.outlook import OutlookService

def load():
    app = load_app()
    session = load_session(app)
    db = load_db()
    auth_service = AuthService(session)
    user_service = UserService(db)
    outlook_service = OutlookService()
    return {
        "app": app,
        "session": session,
        "auth_service": auth_service,
        "user_service": user_service,
        "outlook_service": outlook_service
    }