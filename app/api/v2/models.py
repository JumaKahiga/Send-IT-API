from flask import jsonify
from app.api.database import db


# User roles
customer = "Customer"
site_admin = "Admin"


class UserModel(object):
    """Creating user model"""
    def __init__(self):
        self.user_role = customer

    def new_user(self, ):
        query = "INSERT into users_tb(username, email, password, contact_phone, role)" "VALUES(%s, %s)"

        created_user= self.user_db.append(user_data)
        return created_user

    def single_user(self, user_id):
        for user in users:
            if user["user_id"] == user_id and type(user_id)==int:
                return user
            else:
                return jsonify({'User': 'Not Available'})

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
        return "Inserted successfully"

    def parcels_list(self):
        pass

    # def single_parcel(self, parcel_id):
    #     percels = [parcel for parcel in parcels if parcel["parcel_id"] == parcel_id]
    #     if not percels:
    #         return jsonify({'parcel': 'Not Available'})
    #     else:
    #         return percels[0]

    # def cancel_order(self, parcel_id):
    #     for parcel in parcels:
    #         if parcel["parcel_id"] != parcel_id:
    #             return jsonify({'parcel': "Parcel not found"})
    #         elif parcel["status"] == cancelled:
    #             return jsonify({'parcel': "Order already cancelled"})
    #         elif parcel['parcel_id'] == parcel_id:
    #             parcel.update({"status": cancelled})
    #             return {'parcel': 'Order Cancelled'}

    def specific_user_orders(self, user_id):
        parcel_list= []
        for parcel in self.db:
            if parcel['user_id'] == user_id:
                parcel_list.append(parcel)
        if not parcel_list:
            return {'parcel': 'Not Available'}
        return parcel_list
        		
    def clear(self):
    	self.db = []


