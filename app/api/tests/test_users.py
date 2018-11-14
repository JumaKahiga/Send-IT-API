import unittest
import json
from app.api.tests.test_base import BaseTest



class TestUser(BaseTest):
	"""docstring for TestUser"""
	def test_new_user(self):
		respo= self.client.post('/api/v1/users',data = json.dumps(self.sample_user), content_type='application/json')
		self.assertEqual(respo.status_code, 201)

	def test_single_user(self):
		user_id = self.new_user_id
		respo= self.client.get('/api/v1/users/' + user_id)
		self.assertEqual(respo.status_code, 200)


if __name__ == "__main__":
	unittest.main()