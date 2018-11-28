"""Contain user registration, login, and any other authentication function."""
import hashlib
import json
from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
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

    def get_user_role(self, email):
        """Gets user role during login."""
        db_return = db.fetch_role(email)
        if db_return == None:
            return False
        else:
            user_role = int(db_return[0]["role"])
            return user_role

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
        column = "contact_phone"
        db_return = db.fetch_number(sort_item)
        if db_return == None:
            return True


def admin_required(fn):
    """Limits access of routes to admin."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_dict = get_jwt_identity()
        email = user_dict["email"]
        user_role = password_check.get_user_role(email)
        print(user_role)
        if user_role != 1:
            return jsonify({"message": "Admins only"})
        else:
            return fn(*args, **kwargs)
    return wrapper


# Create instance of PasswordAuth class
password_check = PasswordAuth()
reg_auth = RegAuth()
