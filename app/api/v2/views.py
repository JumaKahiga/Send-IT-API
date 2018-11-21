from flask import request, Blueprint, make_response, jsonify
import json
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from app.api.v2.models import ParcelOrder, UserModel
from app.api.utilities.validators import email_validator


parcel = ParcelOrder()
mteja= UserModel()

#User roles
admin = 1
user = 2

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
		role = user
		if email_validator(email):
			mteja.new_user(username, email, password, contact_phone, role)
			return make_response(jsonify({"message": "User registration successful"}), 201)
		else:
			return jsonify({"message": "Please enter valid email"})


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
		return mteja.user_db


class CreateParcels(Resource):
	def __init__(self):
		self.user_id= 100
		self.parcel_parser= RequestParser()
		self.parcel_parser.add_argument("client_name", type=str, required=True, help="Invalid username. Please try again")
		self.parcel_parser.add_argument("recipient_name", type=str, required=True, help="Invalid username. Please try again")
		self.parcel_parser.add_argument("package_desc", type=str, required=True, help="Please enter valid package details")
		self.parcel_parser.add_argument("location", type=str, required=True, help="Details for where parcel will be collected are invalid")
		self.parcel_parser.add_argument("destination", type=str, required=True, help="Details for where parcel will be delivered are invalid")
		self.parcel_parser.add_argument("pickup_date", type=str, required=True, help="Please enter valid pickup date for the parcel")

	def post(self):
		data = self.parcel_parser.parse_args()
		client_name = data['client_name']
		user_id= self.user_id + 1
		recipient_name = data['recipient_name']
		package_desc = data['package_desc']
		location = data['location']
		destination = data['destination']
		pickup_date = data['pickup_date']
		parcel.new_parcel(client_name, user_id, recipient_name, package_desc, location, destination, pickup_date)
		return make_response(jsonify({"message": "Parcel order created successfully"}), 201)


class AllOrders(Resource):
    def get(self):
        return json.loads(parcel.all_parcels())


class SpecificOrder(Resource):
    def get(self, parcel_id):
    	try:
    		int(parcel_id)
    	except ValueError:
    		return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
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
 			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
 		else:
 			parcel_id= int(parcel_id)

 		updated_order= parcel.cancel_order(parcel_id)
 		return updated_order
 		return make_response(jsonify({"message": "Successfully updated"}))


class UserSpecificOrders(Resource):
	def get(self, user_id):
		try:
			int(user_id)
		except ValueError:
			return make_response(jsonify({"Message": "Invalid user ID"}), 409)
		else:
			user_id= int(user_id)

		single_user_orders= parcel.specific_user_orders(user_id)
		return single_user_orders


v2 = Blueprint('v2', __name__, url_prefix='/api/v2')


api = Api(v2, catch_all_404s= True)


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
