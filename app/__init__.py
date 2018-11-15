from flask import Flask
from app.api.v1.views import v1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    @app.errorhandler(404)
    def page_not_found():
    	return jsonify({"Message": "The requested URL does not exist"})

    @app.errorhandler(505)
    def server_error():
    	return jsonify({"Message": "Something went wrong. Check your inputs and try again"})   
    	 
    return app

