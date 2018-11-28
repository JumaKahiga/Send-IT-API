# Dummy data to be used in tests
parcel_dummy_data = {"client_name": "John Doe",
                     "recipient_name": "Mark Joe",
                     "package_desc": "Television",
                     "location": "Mirema",
                     "destination": "Buruburu",
                     "pickup_date": "12 November 2018"}


parcel_invalid_data = {"client_name": "John 80e",
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

user_token_data = {
    "user_id": 2,
    "username": "Marty Leroy",
    "email": "leroy2@yah.com",
    "password": "pass1234",
    "contact_phone": "0712395609",
    "role": 2
}

user_token_login = {
    "email": "leroy2@yah.com",
    "password": "pass1234",
}


dummy_login = {"email": "leroy2@yah.com",
               "password": "pass1234"}


user_invalid_data1 = {
    "user_id": 5,
    "username": "Thomas Smith",
    "email": "thomas.com",
    "password": "pass1234",
    "contact_phone": "0712345678",
    "role": 1
}

user_invalid_data2 = {
    "user_id": 5,
    "username": "Thomas 5m1th",
    "email": "thomas@gma.com",
    "password": "pass1234",
    "contact_phone": "0712345678",
    "role": 1
}

user_invalid_data3 = {
    "user_id": 5,
    "username": "Thomas 5m1th",
    "email": "thomas@gma.com",
    "contact_phone": "0712345678",
    "role": 1
}

user_invalid_data4 = {
    "user_id": 1,
    "username": "Maureen Demp",
    "email": "maury@yah.com",
    "password": "pass1234",
    "contact_phone": "0712345679",
    "role": 1
}

bad_login = {"email": "sam", "password": "kjl"}



location_sample = {"location": "Oyugis"}
destination_sample = {"destination": "Kangari"}