import unittest
from app import create_app
from app.api.v2.models import ParcelOrder, UserModel
from app.api.database import db

parcels = ParcelOrder()
mteja = UserModel()


parcel_dummy_data= {"parcel_id": 2,
					"client_name": "John Doe", 
					"user_id": 5,
					"recipient_name": "Mark Joe",
					"package_desc": "Television", 
					"location": "Mirema", 
					"destination": "Buruburu", 
					"pickup_date": "12 November 2018", 
					"parcel_status": "Delivered"}

user_dummy_data= {
			"user_id": 5,
            "username": "Thomas Smith",
            "email": "thomas@smith.com",
            "password": "pass1234",
            "contact_phone": "0712345678",
            "role": 1
        }


class BaseTest(unittest.TestCase):
	"""docstring for BaseTest"""
	def setUp(self):
		self.db = db
		self.app= create_app(config="testing")
		self.client= self.app.test_client(self)
		self.parcel_id= str(parcel_dummy_data.get("parcel_id"))
		self.sample_parcel= parcel_dummy_data
		self.sample_user= user_dummy_data
		self.user_id= str(user_dummy_data.get("user_id"))

	def tearDown(self):
		pass
		


