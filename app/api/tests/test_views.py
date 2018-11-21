import unittest
import json
from app.api.tests.test_base import BaseTest



class TestParcel(BaseTest):
	"""Class for unit tests for the ParcelOrder model."""
	def test_new_parcel(self):
		respo= self.client.post('/api/v2/parcel',data = json.dumps(self.sample_parcel), content_type='application/json')
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code,201)
		self.assertEqual(result["message"], "Parcel order created successfully")

	def test_all_parcels(self):
		respo= self.client.get('/api/v2/parcels')
		self.assertEqual(respo.status_code, 200)

	def test_single_parcel(self):
		parcel_id= self.parcel_id
		respo= self.client.get('/api/v1/parcels/' + parcel_id)
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 200)



if __name__ == "__main__":
	unittest.main()