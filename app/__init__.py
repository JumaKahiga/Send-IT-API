from flask import Flask, Blueprint 

def create_app():
	app= Flask(__name__)
	#app.register_blueprint(v1)

	return app