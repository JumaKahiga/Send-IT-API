"""Contain user registration, login, and any other authentication function."""
import hashlib


class PasswordAuth():
    """Contains methods for storing and verifying passwords."""

    def pass_hash_salt(self, password, email):
        """Uses email as salt and then hashes user password using hashlib md5."""
        salted_pass = password + email
        hashed_pass = hashlib.md5(str.encode(salted_pass)).hexdigest()

        return hashed_pass

    def check_pass(self, password, email):
        """Checks if password input is correct."""
        if self.pass_hash_salt(password, email) == hashed_pass:
            return True
        return False


# Create instance of PasswordAuth class
password_check = PasswordAuth()
