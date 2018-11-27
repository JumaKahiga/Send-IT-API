import re


def email_validator(email):
	"""Regex to validate email validator."""
	match= re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.]*\.*[a-zA-Z0-9_.+-]*\.*[a-zA-Z.])", email)
	if match:
		return True
	else:
		return False

def space_checker(data_dict):
	"""Checks a dictionary to ensure all characters are alphabets."""
	d_list = list(data_dict.values())
	for item in d_list:
		item = item.replace(" ", "")
		if item.isalpha() is False:
			return False
	return True

def username_checker(username):
	"""Checks username to avoid blank spaces and special characters."""
	username = username.replace(" ", "")
	if username.isalpha():
		return True
	else:
		return False



