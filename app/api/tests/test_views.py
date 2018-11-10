import unittest
import json
from app.api.tests.test_base import BaseTest



class TestParcel(BaseTest):
	"""docstring for TestParcel"""
	def test_new_parcel(self):
		respo= self.client.post('/api/v1/parcel',data = json.dumps(self.sample_parcel), content_type='application/json')
		self.assertEqual(respo.status_code,201)

	def test_all_parcels(self):
		respo= self.client.get('/api/v1/parcels')
		self.assertEqual(respo.status_code, 200)

	def test_single_parcel(self):
		parcel_id= self.new_parcel_id
		respo= self.client.get('/api/v1/parcels/' + parcel_id)
		self.assertEqual(respo.status_code, 200)

	def test_cancel_order(self):
		parcel_id = self.parcel_id
		respo= self.client.put('api/v1/parcels/' + parcel_id + '/cancel')
		self.assertEqual(respo.status_code, 200)


if __name__ == "__main__":
	unittest.main()