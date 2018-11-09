#Initialize empty list
parcels= []

#Order status after pickup
pending= "Waiting for Courier"
on_transit= "On Transit"
delivered= "Delivered"
cancelled= "Cancelled"

class ParcelOrder(object):
	"""Creating model for parcels"""
	def __init__(self):
		self.db= parcels	
		self.parcel_id= len(self.db)	
		self.parcel_status= pending

	def new_parcel(self, client_name, package_desc, location, destination, pickup_date):
		new_order_data= {
							"parcel_id": self.parcel_id + 1,
							"client_name": client_name,
							"package_desc": package_desc,
							"location": location,
							"destination": destination,
							"sickup_date": pickup_date,
							"Status": self.parcel_status,
		}

		order= self.db.append(new_order_form)
		return order