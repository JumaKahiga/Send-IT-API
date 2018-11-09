from flask import Flask, request, Blueprint, make_response, jsonify
from flask_restful import Resource, Api
from models import ParcelOrder

parcel= ParcelOrder()

class ParcelSingle(Resource):
	"""docstring for ParcelList"""
	def __init__(self):
		pass

	def post(self, parcelID):
		pass

	def get(self, parcelID):
		pass