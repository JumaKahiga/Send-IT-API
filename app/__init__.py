from os import getenv
import datetime
from flask import Flask
from flask_jwt_extended import JWTManager
from app.api.v2.views import v2
from config import config_set

secret_key = getenv('SECRET_KEY')

def create_app(config= "development"):
    app = Flask(__name__)
    app.config.from_object(config_set[config])
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] = secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=2)
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/v2'
    jwt = JWTManager(app)
    return app
