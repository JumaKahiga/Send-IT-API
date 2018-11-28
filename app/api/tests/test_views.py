import unittest
import json
from flask_jwt_extended import jwt_required
from app.api.tests.test_base import BaseTest



class TestParcel(BaseTest):
	"""Class for unit tests for the ParcelOrder model."""
	def test_new_parcel(self):
		"""Tests creation of new parcel"""
		respo= self.client.post('/api/v2/parcel',data = json.dumps(self.sample_parcel), content_type='application/json', headers=self.gen_token())
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code,201)
		self.assertEqual(result["message"], "Parcel order created successfully")
		self.assertEqual(self.sample_parcel['client_name'], result['data']['client_name'])

	def test_all_parcels(self):
		"""Tests fetching all parcels"""
		respo= self.client.get('/api/v2/parcels', headers=self.gen_token())
		self.assertEqual(respo.status_code, 200)

	def test_single_parcel(self):
		"""Tests fetching a single order"""
		parcel_id= self.parcel_id
		respo= self.client.get('/api/v2/parcels/' + parcel_id, headers=self.gen_token())
		self.assertEqual(respo.status_code, 200)

	def test_update_status(self):
		"""Tests updating order status"""
		parcel_id = self.parcel_id
		respo = self.client.put('/api/v2/parcels/' + parcel_id + '/status', data = json.dumps(self.status2), content_type='application/json', headers=self.gen_token())
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 200)

	def test_update_location(self):
		"""Tests updating order location"""
		respo = self.client.put('/api/v2/parcels/' + self.parcel_id + '/presentLocation', data =json.dumps(self.location2), content_type='application/json', headers=self.gen_token())
		result = json.loads(respo.data.decode())
		self.assertEqual(result["message"], "Parcel order location updated successfully")
		self.assertEqual(respo.status_code, 200)

	def test_update_destination(self):
		"""Tests updating order destination"""
		respo = self.client.put('/api/v2/parcels/' + self.parcel_id + '/destination', data =json.dumps(self.destination2), content_type='application/json', headers=self.gen_token())
		result = json.loads(respo.data.decode())
		self.assertEqual(result["message"], "Parcel order destination updated successfully")
		self.assertEqual(respo.status_code, 200)

	def test_user_specific_order(self):
		"""Tests getting all orders for a specific user"""
		user_id = self.user_id
		respo= self.client.get('api/v2/users/' + user_id + '/parcels', headers=self.gen_token())
		self.assertEqual(respo.status_code, 200)


class TestFailParcel(BaseTest):
	"""Test wrong inputs in the ParcelOrder Model."""
	def test_invalid_username(self):
		"""Tests when username has invalid characters."""
		respo= self.client.post('/api/v2/parcel',data = json.dumps(self.invalid_parcel), content_type='application/json', headers=self.gen_token())
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code,400)
		self.assertEqual(result["message"], "Parcel details cannot be empty or have special characters")

	def test_invalid_parcel_id(self):
		"""Tests when parcel ID input is not an integer."""
		parcel_id= self.invalid_parcel_id
		respo= self.client.get('/api/v2/parcels/' + parcel_id, headers=self.gen_token())
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 404)
		self.assertEqual(result["Error"], "Enter valid parcel ID")

	def test_invalid_user_id(self):
		"""Tests invalid user ID when getting all orders for a specific user"""
		user_id = self.invalid_user_id
		respo= self.client.get('api/v2/users/' + user_id + '/parcels', headers=self.gen_token())
		result= json.loads(respo.data.decode())
		self.assertEqual(respo.status_code, 404)
		self.assertEqual(result["Error"], "Invalid user ID")


if __name__ == "__main__":
	unittest.main()