from flask import jsonify
from app.api.database import db

db.create_tables()

# User roles
customer = 2
site_admin = 1


class UserModel(object):
    """Creating user model"""
    def __init__(self):
        self.user_role = customer

    def new_user(self, username, email, password, contact_phone, role):
        new_user_data = {
            "username": username,
            "email": email,
            "password": password,
            "contact_phone": contact_phone,
            "role": customer,
        }

        users_tb = "users_tb"
        new_user_id = "user_id"

        created_user = db.insert(users_tb, new_user_data, new_user_id)
        return created_user


    def single_user(self):
        pass

# Order status after pickup
pending= "Waiting for Courier"
on_transit= "On Transit"
delivered= "Delivered"
cancelled= "Cancelled"


class ParcelOrder():
    """Creating model for parcels"""
    def __init__(self):
        self.parcel_status = pending

    def new_parcel(self,client_name, user_id, recipient_name, package_desc, location, destination, pickup_date):    	
        new_order_data = {
            "client_name": client_name,
            "user_id": user_id,
            "recipient_name": recipient_name,
            "package_desc": package_desc,
            "location": location,
            "destination": destination,
            "pickup_date": pickup_date,
            "status": self.parcel_status,
        }

        parcels_tb = "parcels_tb"
        new_parcel_id = "user_id"

        created_order = db.insert(parcels_tb, new_order_data, new_parcel_id)
        return created_order

    def parcels_list(self):
        pass

    def specific_user_orders(self, user_id):
        pass
        		
    def clear(self):
    	self.db = []

    def cancel_order(self):
        pass

    def specific_user_orders(self):
        pass
        		
    def clear(self):
    	pass