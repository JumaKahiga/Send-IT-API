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
        self.status2 = status_sample
        self.location2 = location_sample
        self.destination2 = destination_sample
        self.sample_user = user_dummy_data
        self.user_data = user_token_data
        self.user_login = user_token_login
        self.sample_admin = admin_dummy_data
        self.admin_data = admin_token_data
        self.admin_login = admin_token_login
        self.invalid_user1 = user_invalid_data1
        self.invalid_user2 = user_invalid_data2
        self.invalid_user3 = user_invalid_data3
        self.invalid_user4 = user_invalid_data4
        self.invalid_user5 = user_invalid_data5
        self.bad_login = bad_login
        self.sample_login = dummy_login
        self.sample_login = dummy_login
        self.user_id = str(user_dummy_data.get("user_id"))
        self.invalid_user_id = "@"

    def gen_token(self):
        """Generates user token to be used during testing"""
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_data),
            content_type='application/json')
        respo = self.client.post('/api/v2/auth/login', data=json.dumps(self.user_login),
            content_type='application/json')
        access_token = json.loads(respo.data.decode())["tokens"]["access_token"]
        log_header = {'Authorization': 'Bearer {}'.format(access_token)}
        return log_header

    def gen_admin_token(self):
        """Generates admin token to be used during testing"""
        self.client.post('/api/v2/auth/admin/signup', data=json.dumps(self.admin_data),
            content_type='application/json')
        respo = self.client.post('/api/v2/auth/login', data=json.dumps(self.admin_login),
            content_type='application/json')
        access_token = json.loads(respo.data.decode())["tokens"]["access_token"]
        log_header = {'Authorization': 'Bearer {}'.format(access_token)}
        return log_header

    def get_parcel_id(self):
        """Gets parcel_id of created dummy parcel"""
        table = "parcels_tb"
        column = "package_desc"
        sort_item = self.sample_parcel["package_desc"]
        parcel_data = db.fetch_specific(table, column, sort_item)
        parcel_id = str(parcel_data[0]["parcel_id"])
        return parcel_id

    def tearDown(self):
        """Removes test data from tables."""
        users_tb1 = "users_tb"
        sort_item1 = "email"
        sort_value1 = self.sample_user["email"]

        db.delete_content(users_tb1, sort_item1, sort_value1)

        users_tb2 = "users_tb"
        sort_item2 = "email"
        sort_value2 = self.sample_admin["email"]

        db.delete_content(users_tb2, sort_item2, sort_value2)

        users_tb3 = "users_tb"
        sort_item3 = "email"
        sort_value3 = self.user_data["email"]

        db.delete_content(users_tb3, sort_item3, sort_value3)

        parcels_tb = "parcels_tb"
        sort_item4 = "package_desc"
        sort_value4 = self.sample_parcel["package_desc"]

        db.delete_content(parcels_tb, sort_item4, sort_value4)


if __name__ == '__main__':
    unittest.main()
