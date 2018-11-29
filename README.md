### Build Badges
[![Build Status](https://travis-ci.org/JumaKahiga/Send-IT-API.svg?branch=develop)](https://travis-ci.org/JumaKahiga/Send-IT-API)[![Coverage Status](https://coveralls.io/repos/github/JumaKahiga/Send-IT-API/badge.svg?branch=develop)](https://coveralls.io/github/JumaKahiga/Send-IT-API?branch=develop)

# sendIT
SendIT is an app for a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories

## Send-IT-API
The [challenge 2](https://github.com/JumaKahiga/Send-IT-API/tree/challenge2) branch has the API version 1 (v1) of the SendIT app that allows creation, editing, and cancellation of parcel delivery orders using non-persistent data (lists)

The default branch, [develop](https://github.com/JumaKahiga/Send-IT-API/tree/develop), has the API version 2 (v2) of the SendIT app that uses a postgres database to store data. In addition, this version contains token-based authentication for users and admin routes. 


### Current two versions are only API

### Current Features/ End Points
1. Fetch all parcel delivery orders (`api/v2/parcels/`)
2. Fetch a specific parcel delivery order (`api/v2/parcels/{parcel_id}`)
3. Fetch all parcel delivery orders by a specific user (`api/v2/users/{user_id}/parcels`)
4. Update status of a specific parcel delivery order (`api/v2/parcels/{parcel_id}/status`)
5. Update location of a specific parcel delivery order (`api/v2/parcels/{parcel_id}/presentLocation`)
6. Update destination of a specific parcel delivery order (`api/v2/parcels/{parcel_id}/destination`)
7. Create a parcel delivery order (`api/v2/parcel/`)
8. Create a user (`api/v2/auth/signup`)
9. Create an admin (`api/v2/auth/admin/signup`)
10. Login user/ admin (`api/v2/auth/login`)

NB: A user only has access to endpoint 2, 3, 6, 7, 8, and 10; the rest are for admin.

### Current version built using
1. Flask-Restful
2. Python
3. Postgres 

### Testing done using
1. Pytest

### Continuous integration
1. Travis CI
2. Coveralls 

### How to install and run on your local machine
1. Clone the repository using the following [link](https://github.com/JumaKahiga/Send-IT-API.git)
2. Pip install requirements.txt
3. In the root folder of the cloned repository, open a terminal/ command prompt window and enter the following command `flask run` 
4. In your browser, navigate to the following url address `http://127.0.0.1:5000/api/v2/auth/signup` to create a new user or
  `http://127.0.0.1:5000/api/v2/auth/admin/signup` to create an admin.
5. Login with the details used for registration on `http://127.0.0.1:5000/api/v2/auth/login`

### A hosted version of the current API version is available on the following Heroku [link](https://sendit-v2-app.herokuapp.com/)

### Documentation for the various endpoints is available on [Postman](https://documenter.getpostman.com/view/5800026/RzfcNCAg)


