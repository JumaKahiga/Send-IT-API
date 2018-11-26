import unittest
import os
from app import create_app
from app.api.v2.models import ParcelOrder, UserModel
from app.api.database import db


# Create instances of models classes to be used in tests
parcels = ParcelOrder()
mteja = UserModel()


# Dummy data to be used in tests
parcel_dummy_data = {"parcel_id": 2,
                     "client_name": "John Doe",
                     "user_id": 5,
                     "recipient_name": "Mark Joe",
                     "package_desc": "Television",
                     "location": "Mirema",
                     "destination": "Buruburu",
                     "pickup_date": "12 November 2018",
                     "parcel_status": "On Transit"}


user_dummy_data = {
    "user_id": 1,
    "username": "Thomas Smith",
    "email": "thomas@smith.com",
    "password": "pass1234",
    "contact_phone": "0712345678",
    "role": 1
}


dummy_login = {"email": "sam@gm.com",
               "password": "kjl"}


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
        self.client = self.app.test_client(self)
        self.parcel_id = str(parcel_dummy_data.get("parcel_id"))
        self.sample_parcel = parcel_dummy_data
        self.status2 = "Delivered"
        self.location2 = location_sample
        self.destination2 = destination_sample
        self.sample_user = user_dummy_data
        self.invalid_user = user_invalid_data
        self.bad_login = bad_login
        self.sample_login = dummy_login
        self.user_id = str(user_dummy_data.get("user_id"))

    def tearDown(self):
        pass
