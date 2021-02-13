from flask import Flask
import config
from werkzeug.middleware.proxy_fix import ProxyFix


def load_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    return app