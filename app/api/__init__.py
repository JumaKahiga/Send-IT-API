"""

from flask import Blueprint
from flask_restful import Api
from app.api.v1.views import ParcelSingle
from app import create_app
create_app()


v1 = Blueprint('v1', ___name__, url_prefix='/api/v1')


api = Api(v1)

api.add_resource(ParcelSingle, '/parcel', strict_slashes= False)

api.add_resource(Parcel, '/parcels/<string:name>', strict_slashes= False)

"""

