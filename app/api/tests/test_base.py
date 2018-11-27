import unittest
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


dummy_login = {"email": "maureen@yah.com",
               "password": "pass1234"}

tokens_dict = {
    'access_token': create_access_token(identity={"email": dummy_login["email"], "user_role": user_dummy_data["role"]}, fresh=True),
    'refresh_token': create_refresh_token(identity={"email": dummy_login["email"], "user_role": user_dummy_data["role"]}),
    }


user_invalid_data = {
    "user_id": 5,
    "username": "Thomas Smith",
    "email": "thomas.com",
    "password": "pass1234",
    "contact_phone": "0712345678",
    "role": 1
}

bad_login = {"email": "sam", "password": "kjl"}

app.app_context().push()


location_sample = {"location": "Oyugis"}
destination_sample = {"destination": "Kangari"}


class BaseTest(unittest.TestCase):
    """docstring for BaseTest"""

    def setUp(self):
        self.db = db
        os.environ["FLASK_ENV"] = "testing"
        self.app = create_app(config="testing")
        app.app_context().push()
        self.client = self.app.test_client(self)
        self.app.testing = True
        self.parcel_id = str(parcel_dummy_data.get("parcel_id"))
        self.sample_parcel = parcel_dummy_data
        self.status2 = "Delivered"
        self.location2 = location_sample
        self.destination2 = destination_sample
        self.sample_user = user_dummy_data
        self.invalid_user = user_invalid_data
        self.bad_login = bad_login
        self.sample_login = dummy_login
        self.access_token = tokens_dict["access_token"]
        self.user_id = str(user_dummy_data.get("user_id"))

    def tearDown(self):
        pass
