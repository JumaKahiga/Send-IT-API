from flask import Flask
from app.api.v2.views import v2
from config import config_set


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config_set[config])
    app.register_blueprint(v2)
    return app
