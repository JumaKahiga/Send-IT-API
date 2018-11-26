"""Contain user registration, login, and any other authentication function."""
import hashlib
import json
from app.api.database import db


class PasswordAuth():
    """Contains methods for storing and verifying passwords."""

    def pass_hash_salt(self, password, email):
        """Uses email as salt and then hashes user password using hashlib md5."""
        salted_pass = password + email
        hashed_pass = hashlib.md5(str.encode(salted_pass)).hexdigest()

        return hashed_pass

    def check_pass(self, email):
        """Checks if password input is correct."""
        users_tb = "users_tb"
        email = "email"
        sort_item = email
        db_return = db.fetch_specific(users_tb, email, sort_item)
        if db_return == []:
            return False
        else:
            hashed_pass = db_return["password"]
            return hashed_pass


# Create instance of PasswordAuth class
password_check = PasswordAuth()
