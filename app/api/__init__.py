from flask import Blueprint 
from flask_restful import Api, Resource
from app.api.v1.views import (classes)

superv1= Blueprint('v1', ___name__, url_prefix='/api/v1')


api= Api(superv1)

api. add_resource(Class, '/parcel/')