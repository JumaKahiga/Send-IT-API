from flask import request, Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from app.api.v1.models import ParcelOrder


parcel = ParcelOrder()


class CreateParcels(Resource):
    def __init__(self):
        pass

    def post(self):
        data = request.get_json()
        client_name = data['client_name']
        package_desc = data['package_desc']
        location = data['location']
        destination = data['destination']
        pickup_date = data['pickup_date']
        parcel.new_parcel(client_name, package_desc, location, destination, pickup_date)
        parcels = parcel.db
        return make_response(jsonify({"message": "Parcel order created successfully"}), 200)


class AllOrders(Resource):
    def __init__(self):
        pass

    def get(self):
        return parcel.db


class SpecificOrder(Resource):
    def __init__(self):
        pass

    def get(self, parcel_id):
        data = request.get_json()
        single_order = parcel.single_parcel(parcel_id)
        return single_order


v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


api = Api(v1)


# Add parcel resources
api.add_resource(CreateParcels, "/parcel", strict_slashes=False)
api.add_resource(AllOrders, "/parcels", strict_slashes=False)
api.add_resource(SpecificOrder, '/parcels/<int:parcel_id>', strict_slashes=False)
