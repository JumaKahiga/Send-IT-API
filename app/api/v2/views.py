from flask import request, Blueprint, make_response, jsonify
import json
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from app.api.v2.models import ParcelOrder, UserModel
from app.api.utilities.validators import email_validator


parcel = ParcelOrder()
mteja = UserModel()

# User roles
admin = 1
user = 2

""" User Models."""


class CreateUser(Resource):
	"""Class for creating users."""

	def __init__(self):
		self.user_parser = RequestParser()
		self.user_parser.add_argument(
			"username", type=str, required=True, help="Username can only consist of letters")
		self.user_parser.add_argument(
			"email", type=str, required=True, help="Invalid email")
		self.user_parser.add_argument(
			"password", required=True, help="Password cannot be empty")
		self.user_parser.add_argument(
			"contact_phone", type=int, required=True, help="Phone number can only be an integer")

	def post(self):
		user_data = self.user_parser.parse_args()
		username = user_data.get("username")
		email = user_data.get("email")
		password = user_data.get("password")
		contact_phone = user_data.get("contact_phone")
		if email_validator(email):
			new_user = mteja.new_user(username, email, password, contact_phone)
			new_user = json.loads(new_user)
			return make_response(jsonify(
				{"message": "User registration successful",
				 "data": new_user}), 201)
		else:
			return make_response(jsonify({"message": "Please enter a valid email"}), 400)


class UserLogin(Resource):

	def __init__(self):
		self.user_parser = RequestParser()
		self.user_parser.add_argument(
			"email", type=str, required=True, help="Invalid email")
		self.user_parser.add_argument(
			"password", required=True, help="Invalid password")

	def post(self):
		"""Method logins user."""
		user_data = self.user_parser.parse_args()
		email = user_data.get("email")
		password = user_data.get("password")

		email_chk = email_validator(email)

		if not email_chk:
			return make_response(jsonify({"message": "Please enter a valid email"}), 400)
		else:
			login_data = mteja.login_user(email, password)

		if login_data == True:
			return make_response(jsonify({"message": "Login successful"}), 200)
		else:
			return make_response(jsonify({"message": "User not found. Please try api/v2/auth/signup"}), 406)


""" Parcel Models."""


class CreateParcels(Resource):
	"""Creates a new parcel order."""

	def __init__(self):
		"""Integrates RequestParser for input validation"""
		self.user_id = 0
		self.parcel_parser = RequestParser()
		self.parcel_parser.add_argument(
			"client_name", type=str, required=True, help="Invalid username. Please try again")
		self.parcel_parser.add_argument(
			"recipient_name", type=str, required=True, help="Invalid username. Please try again")
		self.parcel_parser.add_argument(
			"package_desc", type=str, required=True, help="Please enter valid package details")
		self.parcel_parser.add_argument(
			"location", type=str, required=True, help="Details for where parcel will be collected are invalid")
		self.parcel_parser.add_argument(
			"destination", type=str, required=True, help="Details for where parcel will be delivered are invalid")
		self.parcel_parser.add_argument(
			"pickup_date", type=str, required=True, help="Please enter valid pickup date for the parcel")

	def post(self):
		"""Creates new order based on input given"""
		data = self.parcel_parser.parse_args()
		client_name = data['client_name']
		user_id = self.user_id + 1
		recipient_name = data['recipient_name']
		package_desc = data['package_desc']
		location = data['location']
		destination = data['destination']
		pickup_date = data['pickup_date']
		new_order = parcel.new_parcel(client_name, user_id, recipient_name,
									  package_desc, location, destination, pickup_date)
		new_order = json.loads(new_order)
		return make_response(jsonify({"message": "Parcel order created successfully",
									  "data": new_order}), 201)


class AllOrders(Resource):
	"""Gets all orders"""

	def get(self):
		return json.loads(parcel.all_parcels())


class SpecificOrder(Resource):
	"""Gets a specific order"""

	def get(self, parcel_id):
		try:
			int(parcel_id)
		except ValueError:
			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
		finally:
			parcel_id = int(parcel_id)

		single_order = json.loads(parcel.single_parcel(parcel_id))
		return single_order


class CancelOrder(Resource):

	def put(self, parcel_id):
		try:
			int(parcel_id)
		except ValueError:
			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
		finally:
			parcel_id = int(parcel_id)

		updated_order = parcel.cancel_order(parcel_id)
		return updated_order
		return make_response(jsonify({"message": "Successfully updated"}))


class UserSpecificOrders(Resource):
	"""Gets all orders for a single user"""

	def get(self, user_id):
		try:
			int(user_id)
		except ValueError:
			return make_response(jsonify({"Message": "Invalid user ID"}), 409)
		else:
			user_id = int(user_id)

		single_user_orders = json.loads(parcel.user_orders(user_id))
		return single_user_orders


class UpdateOrderStatus(Resource):
	"""Updating order status."""

	def put(self, parcel_id):
		try:
			int(parcel_id)
		except ValueError:
			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
		finally:
			parcel_id = int(parcel_id)

		updated_order = parcel.update_status(parcel_id)
		return make_response(jsonify({"message": "Parcel order status updated successfully"}), 200)


class UpdateOrderLocation(Resource):
	"""Updating order location"""

	def __init__(self):
		self.location_parser = RequestParser()
		self.location_parser.add_argument(
			"location", type=str, required=True, help="Invalid location details")

	def put(self, parcel_id):
		try:
			int(parcel_id)
		except ValueError:
			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
		finally:
			parcel_id = int(parcel_id)

		data = self.location_parser.parse_args()
		location = data['location']
		parcel_id = parcel_id

		updated_order = parcel.update_location(parcel_id, location)
		return make_response(jsonify({"message": "Parcel order location updated successfully"}), 200)


class UpdateOrderDestination(Resource):
	"""Updating order destination"""

	def __init__(self):
		self.destination_parser = RequestParser()
		self.destination_parser.add_argument(
			"destination", type=str, required=True, help="Invalid destination details")

	def put(self, parcel_id):
		try:
			int(parcel_id)
		except ValueError:
			return make_response(jsonify({"Error": "Enter valid parcel ID"}), 404)
		finally:
			parcel_id = int(parcel_id)

		data = self.destination_parser.parse_args()
		destination = data['destination']
		parcel_id = parcel_id

		updated_order = parcel.update_destination(parcel_id, destination)
		return make_response(jsonify({"message": "Parcel order destination updated successfully"}), 200)

v2 = Blueprint('v2', __name__, url_prefix='/api/v2')


api = Api(v2, catch_all_404s=True)


# Add parcel resources
api.add_resource(CreateParcels, "/parcel", strict_slashes=False)
api.add_resource(AllOrders, "/parcels", strict_slashes=False)
api.add_resource(SpecificOrder, '/parcels/<parcel_id>', strict_slashes=False)
api.add_resource(CancelOrder, '/parcels/<parcel_id>/cancel',
				 strict_slashes=False)
api.add_resource(UpdateOrderStatus,
				 '/parcels/<parcel_id>/status', strict_slashes=False)
api.add_resource(UpdateOrderLocation,
				 '/parcels/<parcel_id>/presentLocation', strict_slashes=False)
api.add_resource(UpdateOrderDestination,
				 '/parcels/<parcel_id>/destination', strict_slashes=False)


# Add user resources
api.add_resource(CreateUser, "/auth/signup", strict_slashes=False)
api.add_resource(UserLogin, '/auth/login', strict_slashes=False)
api.add_resource(UserSpecificOrders,
				 '/users/<user_id>/parcels', strict_slashes=False)
