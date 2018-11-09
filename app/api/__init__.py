from flask import Blueprint 
from flask_restful import Api, Resource
from app.api.v1.views import ParcelSingle

superv1= Blueprint('v1', ___name__, url_prefix='/api/v1')


api= Api(superv1)

api. add_resource(ParcelSingle, '/parcel', strict_slashes= False)

#api.add_resource(Parcel, '/parcels/<string:name>', strict_slashes= False)