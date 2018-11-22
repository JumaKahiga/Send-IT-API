import json
from app.api.database import db

db.create_tables()

# User roles
admin = 1
user = 2


class UserModel(object):
    """Creating user model"""
    def __init__(self):
        self.user_role = user

    def new_user(self, username, email, password, contact_phone, role):
        new_user_data = {
            "username": username,
            "email": email,
            "password": password,
            "contact_phone": contact_phone,
            "role": user,
        }

        users_tb = "users_tb"
        new_user_id = "user_id"

        created_user = db.insert(users_tb, new_user_data, new_user_id)
        return created_user


    def single_user(self):
        pass

# Order status
order_status = {
	"pending" : "Waiting for Courier",
	"on_transit" : "On Transit",
	"delivered" : "Delivered",
	"cancelled": "Cancelled"
}

class ParcelOrder():
    """Creating model for parcels"""
    def __init__(self):
        self.parcel_status = order_status["pending"]
        self.db = db

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
        new_parcel_id = "parcel_id"

        created_order = db.insert(parcels_tb, new_order_data, new_parcel_id)
        return created_order

    def all_parcels(self):
        parcels_tb = "parcels_tb"

        all_orders = db.fetch_all(parcels_tb)
        all_orders = json.dumps(all_orders, default=str)
        return all_orders

    def single_parcel(self, parcel_id):
        parcels_tb = "parcels_tb"
        column = "parcel_id"
        sort_item = parcel_id

        single_order = db.fetch_specific(parcels_tb, column, sort_item)
        single_order = json.dumps(single_order, default=str)
        return single_order

    def update_status(self, parcel_id):
    	parcels_tb = "parcels_tb"
    	column_name = "status"
    	column_value = order_status["delivered"]
    	sort_item = "parcel_id"
    	sort_value = parcel_id

    	updated_order = db.update_details(parcels_tb, column_name, column_value, sort_item, sort_value)
    	show_order = db.fetch_specific(parcels_tb, sort_item, sort_value)
    	return show_order

        		
    def clear(self):
    	self.db = []

    def cancel_order(self):
        pass

    def specific_user_orders(self):
        pass
        		
    def clear(self):
    	pass