import unittest
import json
from app.api.tests.test_base import BaseTest


class TestAdmin(BaseTest):
	"""Tests the Admin signup and login."""

	def test_new_admin(self):
		"""Tests successful creation of a new user."""
		respo = self.client.post(
			'api/v2/auth/signup', data=json.dumps(self.sample_admin), content_type='application/json')
		result = json.loads(respo.data.decode())
		#self.assertEqual(respo.status_code, 201)
		self.assertEqual(result["message"], "User registration successful")
		self.assertEqual(self.sample_admin['username'], result[
						 'data']['username'])

	def test_login_user(self):
		"""Tests successful log in."""
		self.client.post('/api/v2/auth/admin/signup', data=json.dumps(self.admin_data),
            content_type='application/json')
		respo = self.client.post(
			'api/v2/auth/login', data=json.dumps(self.admin_login), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 200)
		self.assertEqual(result["message"], "Login successful")


class TestAdminRoutes(BaseTest):
	"""Tests routes only accessible to admin."""

	def test_all_parcels(self):
		"""Tests fetching all parcels"""
		respo= self.client.get('/api/v2/parcels', headers=self.gen_admin_token())
		self.assertEqual(respo.status_code, 200)

	def test_update_status(self):
		"""Tests updating order status"""
		parcel_id = self.parcel_id
		respo = self.client.put('/api/v2/parcels/' + parcel_id + '/status', data = json.dumps(self.status2), content_type='application/json', headers=self.gen_admin_token())
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 200)

	def test_update_location(self):
		"""Tests updating order location"""
		respo = self.client.put('/api/v2/parcels/' + self.parcel_id + '/presentLocation', data =json.dumps(self.location2), content_type='application/json', headers=self.gen_admin_token())
		result = json.loads(respo.data.decode())
		self.assertEqual(result["message"], "Parcel order location updated successfully")
		self.assertEqual(respo.status_code, 200)


class TestFailAdminRoute(BaseTest):
	"""Tests when user tries accessing an admin route."""

	def test_update_location(self):
		"""Tests updating order location"""
		respo = self.client.put('/api/v2/parcels/' + self.parcel_id + '/presentLocation', data =json.dumps(self.location2), content_type='application/json', headers=self.gen_token())
		result = json.loads(respo.data.decode())
		self.assertEqual(result["message"], "Admins only")

class TestAdminFail(BaseTest):
	"""Tests unsuccessful admin registration."""

	def test_invalid_email(self):
		"""Tests failed sign up when email input is invalid."""
		respo = self.client.post(
			'api/v2/auth/admin/signup', data=json.dumps(self.invalid_user1), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"], "Please enter a valid email")

	def test_invalid_username(self):
		"""Tests failed sign up when username input is invalid."""
		respo = self.client.post(
			'api/v2/auth/admin/signup', data=json.dumps(self.invalid_user2), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"], "Username cannot be blank spaces or have special characters")

	def test_empty_password(self):
		"""Tests failed sign up when password input is empty."""
		respo = self.client.post(
			'api/v2/auth/admin/signup', data=json.dumps(self.invalid_user3), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"]["password"], "Password cannot be empty")

	def test_admin_exists(self):
		"""Tests failed sign up when admin is already registered."""
		self.client.post(
			'api/v2/auth/admin/signup', data=json.dumps(self.sample_admin), content_type='application/json')
		respo = self.client.post(
			'api/v2/auth/signup', data=json.dumps(self.sample_admin), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"], "User already exists")

	def test_phone_exists(self):
		"""Tests failed sign up when phone number is already registered."""
		self.client.post(
			'api/v2/auth/signup', data=json.dumps(self.sample_admin), content_type='application/json')
		respo = self.client.post(
			'api/v2/auth/signup', data=json.dumps(self.invalid_user5), content_type='application/json')
		result = json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 400)
		self.assertEqual(result["message"], "Phone number is registered to another user")