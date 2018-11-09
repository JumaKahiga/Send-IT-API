import unittest
import json
from app.api.tests.test_base import BaseTest


parcel_dummy_data= {"parcel_id": "100", 
					"client_name": "John Doe", 
					"package_desc": "Television", 
					"location": "Mirema", 
					"destination": "Buruburu", 
					"pickup_date": "12 November 2018", 
					"parcel_status": "Delivered"}

class TestParcel(BaseTest):
	"""docstring for TestParcel"""
	def test_new_parcel(self):
		respo= self.client.post('/api/v1/parcel',data = json.dumps(parcel_dummy_data), content_type='application/json')
		self.assertEqual(respo.status_code,200)


	def test_single_parcel(self):
		respo= self.client.get('/api/v1/parcels')
		self.assertEqual(respo.status_code, 200)


if __name__ == "__main__":
	unittest.main()