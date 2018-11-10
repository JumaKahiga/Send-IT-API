users= []

# User roles
customer = "Customer"
site_admin = "Admin"


class UserModel(object):
    """Creating user model"""
    def __init__(self):
        self.udb = users
        self.user_id = len(self.udb)
        self.new_user_id= self.user_id + 1
        self.user_role = customer

    def new_user(self, uname, email, password, contact_phone):
        user_data = {
            "user_id": self.user_id + 1,
            "uname": uname,
            "email": email,
            "password": password,
            "contact_phone": contact_phone,
        }

        created_user = self.udb.append(user_data)
        return created_user

    def single_user(self, user_id):
        for user in users:
            if user["user_id"] == user_id:
                return user
            else:
                return {'User': 'Not Available'}, 404


parcels = []

# Order status after pickup
pending= "Waiting for Courier"
on_transit= "On Transit"
delivered= "Delivered"
cancelled= "Cancelled"


class ParcelOrder(UserModel):
    """Creating model for parcels"""
    def __init__(self):
        self.db = parcels
        self.parcel_id = len(self.db)
        self.new_parcel_id= self.parcel_id + 1
        self.parcel_status = pending
        self.user_id= user_id

    def new_parcel(self, client_name, package_desc, location, destination, pickup_date):
        new_order_data = {
            "parcel_id": self.new_parcel_id,
            "client_name": client_name,
            "user_id": user_id,
            "package_description": package_desc,
            "location": location,
            "destination": destination,
            "pickup_date": pickup_date,
            "status": self.parcel_status,
        }

        order= self.db.append(new_order_data)
        return order

    def parcels_list(self):
        return self.db

    def single_parcel(self, parcel_id):
        for parcel in parcels:
            if parcel["parcel_id"]== parcel_id:
                return parcel
            else:
                return {'parcel': 'Not Available'}, 404

    def cancel_order(self, parcel_id):
        for parcel in parcels:
            if parcel["status"] == delivered:
                return {'parcel': "Cannot be cancelled. Already delivered"}
            elif parcel['parcel_id'] == parcel_id:
                parcel.update({"status": cancelled})
                return {'parcel': 'Order Cancelled'}

    def specific_user_orders(self, user_id):
        for parcel in parcels:
        	if parcel["user_id"] == user_id:
        		return parcel
        	else:
        		return {'parcel': 'Not Available'}, 404
    def clear(self):
    	self.db = []


