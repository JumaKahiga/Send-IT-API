"""Contains user registration, login, and any other authentication function."""
import hashlib


class PasswordAuth():
	"""Contains methods for storing and verifying passwords."""

	def pass_hash_salt(self, password, email, user_id):
		"""Uses email as salt and then hashes user password using hashlib md5."""
		salted_pass = password + email + user_id
		hashed_pass = hashlib.md5(str.encode(salted_pass)).hexdigest()

		return hashed_pass

	def check_pass(self, password, email, user_id):
		"""Checks if password input is correct."""
		if pass_hash_salt(password, email, user_id) == hashed_pass:
			return True
		return False


# Create instance of PasswordAuth class
password_check = PasswordAuth()


