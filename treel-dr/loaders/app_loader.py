from flask import Flask
from config import SESSION_TYPE, SECRET_KEY
from werkzeug.middleware.proxy_fix import ProxyFix


def load_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = SESSION_TYPE
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    return app