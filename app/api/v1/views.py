from flask import request, Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from app.api.v1.models import ParcelOrder, UserModel


parcel = ParcelOrder()
mteja= UserModel()



class CreateUser(Resource):
	def __init__(self):
		self.user_parser= RequestParser()
		self.user_parser.add_argument("username", type=str, required=True, help="Username can only consist of letters")
		self.user_parser.add_argument("email", type=str, required=True, help="Invalid email")
		self.user_parser.add_argument("password", required=True, help="Password cannot be empty")
		self.user_parser.add_argument("contact_phone", type=int, required=True, help="Phone number can only be an integer")

	def post(self):
		user_data = self.user_parser.parse_args()
		username = user_data.get("username")
		email = user_data.get("email")
		password = user_data.get("password")
		contact_phone = user_data.get("contact_phone")
		mteja.new_user(username, email, password, contact_phone)
		return make_response(jsonify({"message": "User registration successful"}), 201)


class SpecificUser(Resource):
    def get(self, user_id):
        data = request.get_json()
        try:
        	int(user_id)
        except ValueError:
        	return make_response(jsonify({"Error": "Please enter a valid User ID"}))
        else:
        	user_id= int(user_id)

        single_user = mteja.single_user(user_id)
        return single_user


class AllUsers(Resource):
	def get(self):
		return mteja.udb


class CreateParcels(Resource):
	def __init__(self):
		self.user_id= 100

    def post(self):
        data = request.get_json()
        client_name = data['client_name']
        user_id= self.user_id + 1
        package_desc = data['package_desc']
        location = data['location']
        destination = data['destination']
        pickup_date = data['pickup_date']
        parcel.new_parcel(client_name, package_desc, location, destination, pickup_date)
        parcels = parcel.db
        return make_response(jsonify({"message": "Parcel order created successfully"}), 201)


class AllOrders(Resource):
    def get(self):
        return parcel.db


class SpecificOrder(Resource):
    def get(self, parcel_id):
    	try:
    		int(parcel_id)
    	except ValueError:
    		return make_response(jsonify({"Error": "Enter valid parcel ID"}), 409)
    	else:
    		parcel_id= int(parcel_id)

    	single_order = parcel.single_parcel(parcel_id)
    	print(parcel_id)
    	return single_order


class CancelOrder(Resource):
 	def put(self, parcel_id):
 		try:
 			int(parcel_id)
 		except ValueError:
 			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 409)
 		else:
 			parcel_id= int(parcel_id)

 		updated_order= parcel.cancel_order(parcel_id)
 		return updated_order
 		return make_response(jsonify({"message": "Parcel order cancelled"}), 200)


class UserSpecificOrders(Resource):
	def get(self, user_id):
		single_user_orders= parcel.specific_user_orders(user_id)
		return single_user_orders


v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


api = Api(v1, catch_all_404s= True)


# Add parcel resources
api.add_resource(CreateParcels, "/parcel", strict_slashes= False)
api.add_resource(AllOrders, "/parcels", strict_slashes= False)
api.add_resource(SpecificOrder, '/parcels/<parcel_id>', strict_slashes= False)
api.add_resource(CancelOrder, '/parcels/<parcel_id>/cancel', strict_slashes= False)


# Add user resources
api.add_resource(CreateUser, "/users", strict_slashes= False)
api.add_resource(AllUsers, "/users/all", strict_slashes= False)
api.add_resource(SpecificUser, '/users/<user_id>', strict_slashes= False)
api.add_resource(UserSpecificOrders, '/users/<user_id>/parcels', strict_slashes= False)
