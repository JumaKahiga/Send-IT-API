import unittest
import json
from test_base import BaseTest


class TestParcel(BaseTest):
	"""docstring for TestParcel"""
	def test_new_parcel(self):
		respo= self.client.post('/api/v1/parcels',data = json.dumps(self.test_parcel), content_type='application/json')
		self.assertEqual(resp.status_code,200)


	def test_single_parcel(self):
		respo= self.client.get('/api/v1/parcels')
		self.assertEqual(respo.status_code, 200)

		