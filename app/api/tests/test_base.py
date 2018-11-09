import unittest
from app import create_app
from api.v1.models import ParcelOrder

parcels = ParcelOrder()
parcel_dummy_data= {"parcel_id": "100", 
					"client_name": "John Doe", 
					"package_desc": "Television", 
					"location": "Mirema", 
					"destination": "Buruburu", 
					"pickup_date": "12 November 2018", 
					"parcel_status": "Delivered"}

class BaseTest(unittest.TestCase):
	"""docstring for BaseTest"""
	def _setUp(self):
		self.app= create_app()
		self.client= self.app.test_client()
		self.test_parcel= parcel_dummy_data

	def tearDown(self):
		parcels.db.clear()
		


