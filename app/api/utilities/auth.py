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

    def check_pass(self, hashed_pass):
        """Checks if password input is correct."""
        db_return = db.fetch_pass(hashed_pass)
        if db_return == None:
            return False
        else:
            hashed_pass = db_return["password"]
            return hashed_pass

class RegAuth():
    """Checks if user already exists."""

    def email_auth(self, email):
        """Checks if email is already registered."""
        sort_item = email
        column = "email"
        db_return = db.fetch_single(column, sort_item)
        if db_return == None:
            return True

    def phone_auth(self, contact_phone):
        """Checks if phone number is already registered."""
        sort_item = contact_phone
        print(sort_item)
        column = "contact_phone"
        db_return = db.fetch_number(sort_item)
        if db_return == None:
            return True


# Create instance of PasswordAuth class
password_check = PasswordAuth()
reg_auth = RegAuth()
