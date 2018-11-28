import unittest
import json
import os
from flask_jwt_extended import create_access_token, create_refresh_token
from app import create_app
from app.api.v2.models import ParcelOrder, UserModel
from app.api.database import db


# Create instances of models classes to be used in tests
parcels = ParcelOrder()
mteja = UserModel()


# Dummy data to be used in tests
parcel_dummy_data = {"client_name": "John Doe",
                     "recipient_name": "Mark Joe",
                     "package_desc": "Television",
                     "location": "Mirema",
                     "destination": "Buruburu",
                     "pickup_date": "12 November 2018"}


user_dummy_data = {
    "user_id": 1,
    "username": "Maureen Dempsy",
    "email": "maureen@yah.com",
    "password": "pass1234",
    "contact_phone": "0712345679",
    "role": 1
}

user_token_data = {
    "user_id": 1,
    "username": "Marty Leroy",
    "email": "leroy2@yah.com",
    "password": "pass1234",
    "contact_phone": "0712395609",
    "role": 2
}

user_token_login = {
    "email": "leroy2@yah.com",
    "password": "pass1234",
}


dummy_login = {"email": "leroy2@yah.com",
               "password": "pass1234"}


user_invalid_data = {
    "user_id": 5,
    "username": "Thomas Smith",
    "email": "thomas.com",
    "password": "pass1234",
    "contact_phone": "0712345678",
    "role": 1
}

bad_login = {"email": "sam", "password": "kjl"}



location_sample = {"location": "Oyugis"}
destination_sample = {"destination": "Kangari"}


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
        self.sample_parcel = parcel_dummy_data
        self.status2 = "Delivered"
        self.location2 = location_sample
        self.destination2 = destination_sample
        self.sample_user = user_dummy_data
        self.user_data = user_token_data
        self.user_login = user_token_login
        self.invalid_user = user_invalid_data
        self.bad_login = bad_login
        self.sample_login = dummy_login
        # self.access_token = tokens_dict["access_token"]
        self.user_id = str(user_dummy_data.get("user_id"))

    def gen_token(self):
        """Generates token to be used during testing"""
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user_data),
            content_type='application/json')
        respo = self.client.post('/api/v2/auth/login', data=json.dumps(self.user_login),
            content_type='application/json')
        access_token = json.loads(respo.data.decode())["tokens"]["access_token"]
        print(access_token)
        log_header = {'Authorization': 'Bearer {}'.format(access_token)}
        return log_header

    def tearDown(self):
        users_tb = "users_tb"
        sort_item = "email"
        sort_value = self.user_data["email"]

        #db.delete_content(users_tb, sort_item, sort_value)


if __name__ == '__main__':
    unittest.main()
