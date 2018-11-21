from flask import jsonify
from app.api.tests.k import devconfig as config_desc
from app.api.database import db

db.create_tables()

# User roles
customer = "Customer"
site_admin = "Admin"


class UserModel(object):
    """Creating user model"""
    def __init__(self):
        self.user_role = customer

    def new_user(self, ):
        pass:

    def single_user(self, user_id):
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

        order= db.insert(parcels_tb, new_order_data)
        return "Parcel created successfully"

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