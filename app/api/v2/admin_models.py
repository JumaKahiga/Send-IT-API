"""Contains models for the app."""

import json
from app.api.database import db
from app.api.utilities.auth import password_check

# User roles
user_roles = {"admin": 1, "user": 2}


class AdminModel(object):
    """Model for Admin."""

    def __init__(self):
        self.user_role = user_roles["admin"]

    def new_user(self, username, email, password, contact_phone):
        """Method creates new user."""
        user_data = {
            "username": username,
            "email": email,
            "password": password,
            "contact_phone": contact_phone,
            "role": self.user_role,
        }

        user_data["password"] = password_check.pass_hash_salt(password, email)

        users_tb = "users_tb"
        to_return = {
            "username": "username",
            "email": "email",
        }

        created_user = db.insert(users_tb, user_data, to_return)
        created_user = json.dumps(created_user, default=str)
        return created_user