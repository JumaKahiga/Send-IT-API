from flask import request, Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from app.api.v1.models import ParcelOrder, UserModel


parcel = ParcelOrder()
mteja= UserModel()


class CreateUser(Resource):
	def __init__(self):
		pass

	def post(self):
		data = request.get_json()
		uname = data['uname']
		email = data['email']
		password = data['password']
		contact_phone = data['contact_phone']
		mteja.new_user(uname, email, password, contact_phone)
		users= mteja.udb
		return make_response(jsonify({"message": "User registration successful"}), 201)


class SpecificUser(Resource):
    def __init__(self):
        pass

    def get(self, user_id):
        data = request.get_json()
        single_user = mteja.single_user(user_id)
        return single_user


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
        return make_response(jsonify({"message": "Parcel order created successfully"}), 201)


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


class CancelOrder(Resource):
 	def __init__(self):
 		pass

 	def put(self, parcel_id):
 		updated_order= parcel.cancel_order(parcel_id)
 		return updated_order
 		return make_response(jsonify({"message": "Parcel order cancelled"}), 200)


v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


api = Api(v1)


# Add parcel resources
api.add_resource(CreateParcels, "/parcel", strict_slashes=False)
api.add_resource(AllOrders, "/parcels", strict_slashes=False)
api.add_resource(SpecificOrder, '/parcels/<int:parcel_id>', strict_slashes=False)
api.add_resource(CancelOrder, '/parcels/<int:parcel_id>/cancel', strict_slashes=False)

# Add user resources
api.add_resource(CreateUser, "/users", strict_slashes=False)
api.add_resource(SpecificUser, '/users/<int:user_id>', strict_slashes=False)
