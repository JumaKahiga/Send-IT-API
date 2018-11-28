import unittest
import json
from app.api.tests.test_base import BaseTest


class TestUserSuccess(BaseTest):
	"""Tests the User model."""

	def test_new_user(self):
		"""Tests successful creation of a new user."""
		respo = self.client.post(
			'api/v2/auth/signup', data=json.dumps(self.sample_user), content_type='application/json')
		result = json.loads(respo.data.decode())
		#self.assertEqual(respo.status_code, 201)
		self.assertEqual(result["message"], "User registration successful")
		self.assertEqual(self.sample_user['username'], result[
						 'data']['username'])

	def test_login_user(self):
		"""Tests successful log in."""
		self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_data),
            content_type='application/json')
		respo = self.client.post(
			'api/v2/auth/login', data=json.dumps(self.sample_login), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 200)
		self.assertEqual(result["message"], "Login successful")


class TestUserFail(BaseTest):
	"""Tests unsuccessful registration and sign in."""

	def test_failed_signup(self):
		"""Tests failed sign up when email input is invalid."""
		respo = self.client.post(
			'api/v2/auth/signup', data=json.dumps(self.invalid_user), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"], "Please enter a valid email")

	def test_failed_login(self):
		"""Tests failed sign in."""
		respo = self.client.post(
			'api/v2/auth/login', data=json.dumps(self.bad_login), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"], "Please enter a valid email")


if __name__ == "__main__":
	unittest.main()
