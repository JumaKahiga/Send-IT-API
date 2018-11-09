from flask import Flask, request, Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from models import ParcelOrder

parcel= ParcelOrder()

class ParcelSingle(Resource):
	"""docstring for ParcelList"""
	def __init__(self):
		pass

	def post(self, parcelID):
		data= request.get_json()
		client_name= data['client_name']
		package_desc= data['package_desc']
		location= data['location']
		destination= data['destination']
		pickup_date= data['pickup_date']

		parcel.new_parcel(client_name, package_desc, location, destination, pickup_date)
		parcels= parcels.db
		return make_response(jsonify({
			"message": "Parcel order created successfully"
			}), 200)

	def get(self, parcelID):
		pass
		
