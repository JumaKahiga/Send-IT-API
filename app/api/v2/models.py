"""Contains models for the app."""

import json
from app.api.database import db
from app.api.utilities.auth import password_check

# User roles
user_roles = {"admin": 1, "user": 2}


class UserModel(object):
    """Model for Users."""

    def __init__(self):
        self.user_role = user_roles["user"]

    def new_user(self, username, email, password, contact_phone):
        """Method creates new user."""
        user_data = {
            "username": username,
            "email": email,
            "password": password,
            "contact_phone": contact_phone,
            "role": self.user_role,
        }

        user_data["password"] = password_check.pass_hash_salt(password, email)

        users_tb = "users_tb"
        to_return = {
            "username": "username",
            "email": "email",
        }

        created_user = db.insert(users_tb, user_data, to_return)
        created_user = json.dumps(created_user, default=str)
        return created_user

    def login_user(self, email, password):
        """Method for login user"""
        hashed_pass = password_check.pass_hash_salt(password, email)
        db_chk = password_check.check_pass(hashed_pass)

        if db_chk == "False":
            unregistered_user = "User not available"
        elif db_chk != hashed_pass:
            wrong_details = "Wrong login details"
            return wrong_details
        elif db_chk == hashed_pass:
            correct_details = "Login succesful"
            return True
        else:
            unrecognized_resp = "Error recognizing the request"
            return unrecognized_resp


# Order status
order_status = {
    "pending": "Waiting for Courier",
    "on_transit": "On Transit",
    "delivered": "Delivered",
    "cancelled": "Cancelled"
}


class ParcelOrder():
    """Model for creating, getting, and updating parcels."""

    def __init__(self):
        self.parcel_status = order_status["pending"]

    def get_user_id(self, email):
        """Gets user_id of current user to be recorded with a new order"""
        column = "user_id"
        sort_item = email
        db_chk = db.fetch_single(column, sort_item)
        return db_chk["user_id"]

    def new_parcel(self, client_name, user_id, recipient_name,
                   package_desc, location, destination, pickup_date):
        new_order_data = {
            "client_name": client_name,
            "user_id": user_id,
            "recipient_name": recipient_name,
            "package_desc": package_desc,
            "location": location,
            "destination": destination,
            "pickup_date": pickup_date,
            "status": self.parcel_status}

        parcels_tb = "parcels_tb"
        to_return = {
            "client_name": "client_name",
            "package_desc": "package_desc",
        }
        
        created_order = db.insert(parcels_tb, new_order_data, to_return)
        created_order = json.dumps(created_order)
        return created_order

    def all_parcels(self):
        """Fetches all orders"""
        parcels_tb = "parcels_tb"

        all_orders = db.fetch_all(parcels_tb)
        all_orders = json.dumps(all_orders, default=str)
        return all_orders

    def single_parcel(self, parcel_id):
        """Fetches single order based on parcel_id"""
        parcels_tb = "parcels_tb"
        column = "parcel_id"
        sort_item = parcel_id

        single_order = db.fetch_specific(parcels_tb, column, sort_item)
        single_order = json.dumps(single_order, default=str)
        return single_order

    def update_status(self, parcel_id, status):
        """Updates status for order with the specified parcel_id"""
        parcels_tb = "parcels_tb"
        column_name = "status"
        column_value = status
        sort_item = "parcel_id"
        sort_value = parcel_id

        db_chk = db.fetch_specific(parcels_tb, sort_item, sort_value)
        if db_chk == []:
            return None
        elif db_chk[0]["status"] != status:
            db.update_details(parcels_tb, column_name,
                  column_value, sort_item, sort_value)
            show_order = db.fetch_specific(parcels_tb, sort_item, sort_value)
            return show_order
        else:
            return False

    def update_location(self, parcel_id, location):
        """Updates location for order with the specified parcel_id"""
        parcels_tb = "parcels_tb"
        column_name = "location"
        column_value = location
        sort_item = "parcel_id"
        sort_value = parcel_id

        db_chk = db.fetch_specific(parcels_tb, sort_item, sort_value)
        if db_chk == []:
            return None
        elif db_chk[0]["location"] != location:
            db.update_details(parcels_tb, column_name,
                  column_value, sort_item, sort_value)
            show_order = db.fetch_specific(parcels_tb, sort_item, sort_value)
            return show_order
        else:
            return False

    def update_destination(self, parcel_id, destination):
        """Updates destination for order with the specified parcel_id"""
        parcels_tb = "parcels_tb"
        column_name = "destination"
        column_value = destination
        sort_item = "parcel_id"
        sort_value = parcel_id

        db_chk = db.fetch_specific(parcels_tb, sort_item, sort_value)
        if db_chk == []:
            return None
        elif db_chk[0]["destination"] != destination:
            db.update_details(parcels_tb, column_name,
                  column_value, sort_item, sort_value)
            show_order = db.fetch_specific(parcels_tb, sort_item, sort_value)
            return show_order
        else:
            return False

    def user_orders(self, user_id):
        """Fetches orders for a specific user"""
        parcels_tb = "parcels_tb"
        column = "user_id"
        sort_item = user_id

        user_orders = db.fetch_specific(parcels_tb, column, sort_item)
        user_orders = json.dumps(user_orders, default=str)
        return user_orders

    def clear(self):
        self.db = []

    def cancel_order(self):
        pass
