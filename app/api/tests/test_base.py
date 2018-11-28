import unittest
import json
import os
from flask_jwt_extended import create_access_token, create_refresh_token
from app import create_app
from app.api.v2.models import ParcelOrder, UserModel
from app.api.database import db
from .dummy_data import *


# Create instances of models classes to be used in tests
parcels = ParcelOrder()
mteja = UserModel()


class BaseTest(unittest.TestCase):
    """docstring for BaseTest"""

    def setUp(self):
        self.db = db
        os.environ["FLASK_ENV"] = "testing"
        self.app = create_app(config="testing")
        self.app.app_context().push()
        self.client = self.app.test_client(self)
        self.app.testing = True
        self.parcel_id = "1"
        self.invalid_parcel_id = "n"
        self.sample_parcel = parcel_dummy_data
        self.invalid_parcel = parcel_invalid_data
        self.status2 = "Delivered"
        self.location2 = location_sample
        self.destination2 = destination_sample
        self.sample_user = user_dummy_data
        self.user_data = user_token_data
        self.user_login = user_token_login
        self.invalid_user1 = user_invalid_data1
        self.invalid_user2 = user_invalid_data2
        self.invalid_user3 = user_invalid_data3
        self.invalid_user4 = user_invalid_data4
        self.bad_login = bad_login
        self.sample_login = dummy_login
        self.user_id = str(user_dummy_data.get("user_id"))
        self.invalid_user_id = "@"

    def gen_token(self):
        """Generates token to be used during testing"""
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_data),
            content_type='application/json')
        respo = self.client.post('/api/v2/auth/login', data=json.dumps(self.user_login),
            content_type='application/json')
        access_token = json.loads(respo.data.decode())["tokens"]["access_token"]
        log_header = {'Authorization': 'Bearer {}'.format(access_token)}
        return log_header

    def tearDown(self):
        """Removes test data from tables."""
        users_tb = "users_tb"
        sort_item = "email"
        sort_value = self.sample_user["email"]

        db.delete_content(users_tb, sort_item, sort_value)


if __name__ == '__main__':
    unittest.main()
