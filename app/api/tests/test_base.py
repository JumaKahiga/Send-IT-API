import unittest
from app import create_app
from app.api.v1.models import ParcelOrder, UserModel


parcels = ParcelOrder()
mteja= UserModel()


parcel_dummy_data= {"client_name": "John Doe", 
					"user_id": 5,
					"package_desc": "Television", 
					"location": "Mirema", 
					"destination": "Buruburu", 
					"pickup_date": "12 November 2018", 
					"parcel_status": "Delivered"}


user_dummy_data= {
            "uname": "Thomas Smith",
            "email": "thomas@smith.com",
            "password": "pass1234",
            "contact_phone": "0712345678",
        }


class BaseTest(unittest.TestCase):
	"""docstring for BaseTest"""
	def setUp(self):
		self.app= create_app()
		self.client= self.app.test_client(self)
		self.sample_parcel= parcel_dummy_data
		self.new_parcel_id= str(parcels.new_parcel_id)
		self.parcel_id= str(parcels.parcel_id)
		self.sample_user= user_dummy_data
		self.new_user_id= str(mteja.new_user_id)

	def tearDown(self):
		parcels.clear()
		


