import psycopg2
from psycopg2.extras import RealDictCursor
import os
from config import config_set

config_desc = os.getenv('FLASK_ENV')

class DbConnections():
	"""Connect to the database"""

	def __init__(self):
		db_choice = config_set[config_desc]
		self.connect = psycopg2.connect(
			database = db_choice().DBNAME,
			user = db_choice().DBUSER,
			password = db_choice().DBPASS,
			host = db_choice().DBHOST)
		self.cur = self.connect.cursor(cursor_factory = RealDictCursor)

	def create_tables(self):
		users_tb = """ CREATE TABLE if not exists users_tb (
				user_id serial PRIMARY KEY NOT NULL,
				username varchar NOT NULL,
				email varchar NOT NULL,
				password varchar NOT NULL,
				contact_phone int NOT NULL,
				role varchar NOT NULL) """

		parcels_tb = """ CREATE TABLE if not exists parcels_tb (
				parcel_id serial PRIMARY KEY,
				client_name varchar NOT NULL,
				user_id int NOT NULL,
				recipient_name varchar NOT NULL,
				package_desc varchar NOT NULL,
				location varchar NOT NULL,
				destination varchar NOT NULL,
				pickup_date varchar NOT NULL,
				status varchar NOT NULL) """

		queries = [users_tb, parcels_tb]
		for query in queries:
			try:
				self.cur.execute(query)
			except (Exception, psycopg2.DatabaseError) as e:
				print("Error connecting to database", e)
			finally:
				self.connect.commit()

	def drop_tables(self):
		query = """ DROP TABLE IF EXISTS users_tb, parcels_tb CASCADE """
		self.cur.execute(query)
		self.connect.commit()


	def insert(self, table, payload, return_id):
		columns = ", ".join(payload.keys())
		values = "','".join(map(str, payload.values()))


		result = """ INSERT INTO {} ({}) VALUES ('{}') RETURNING {}""".format(table, columns, values, return_id)
		result = self.cur.execute(result)
		self.connect.commit()
		return result

	def fetch_all(self, table):
		result_1 = """ SELECT * FROM {} """.format(table)
		self.cur.execute(result_1)
		result_2 = self.cur.fetchall()
		return result_2

	def fetch_specific(self, table, column, sort_item):
		result = """ SELECT * FROM {} WHERE {} = '{}'""".format(table, column, sort_item)
		self.cur.execute(result)
		result = self.cur.fetchall()
		return result

	def update_details(self, table, column_name, column_value, sort_item, sort_value):
		"""Updates table column values for a row matching a specific parameter"""
		result = """ UPDATE {} SET {} = '{}' WHERE {} = {} """.format(table, column_name, column_value, sort_item, sort_value)
		self.cur.execute(result)
		self.connect.commit()
		return result


	def execute(self, query):
		try:
			self.cur.execute(query)
			self.connect.commit()
			return self.cur
		except (Exception, psycopg2.DatabaseError) as e:
			print("Error connecting to database", e)

	def close_connection(self):
		self.cur.close()
		self.connect.close()


db = DbConnections()
