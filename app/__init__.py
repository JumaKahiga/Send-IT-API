from flask import Flask
from flask_cors import CORS
from os import getenv
from app.api.v2.views import v2
from config import config_set


def create_app(config="development"):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_set[config])
    app.register_blueprint(v2)
    return app

