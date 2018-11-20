import unittest
import json
from app.api.tests.test_base import BaseTest



class TestParcel(BaseTest):
	"""docstring for TestParcel"""
	def test_new_parcel(self):
		respo= self.client.post('/api/v2/parcel',data = json.dumps(self.sample_parcel), content_type='application/json')
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code,201)
		self.assertEqual(result["message"], "Parcel order created successfully")


if __name__ == "__main__":
	unittest.main()