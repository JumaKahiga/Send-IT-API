import re

def email_validator(email):
    match= re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.]*\.*[a-zA-Z0-9_.+-]*\.*[a-zA-Z.])", email)
    if match:
        return True
    else:
        return False