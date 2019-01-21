import os

class MainConfig():
	"""Configuration class"""
	DEBUG = False
	TESTING = True
	SECRET_KEY = "andela"
	DBNAME = "sendit_db"
	DBUSER = "sendit_admin"
	DBHOST = "localhost"
	DBPASS = "andela"


class DevelopmentConfig():
	"""Development configuration"""
	DEBUG = True
	DB_URL = "postgresql://sendit_admin:password@localhost/sendit_db"
	TESTING = True
	SECRET_KEY = "andela"
	DBNAME = "sendit_db"
	DBUSER = "sendit_admin"
	DBHOST = "localhost"
	DBPASS = "andela"


class ProductionConfig():
	"""Production configuration"""
	DB_URL = os.getenv('DB_URL')
	DBNAME = os.getenv('DBNAME')
	DBUSER = os.getenv('DBUSER')
	DBHOST = os.getenv('DBHOST')
	DBPASS = os.getenv('DBPASS')


class TestingConfig(MainConfig):
	DEBUG = True
	DBNAME = "sendit_test"
	DBUSER = "postgres"
	DBHOST = "localhost"
	DBPASS = "andela"
	DB_URL = "postgresql://sendit_admin:password@localhost/sendit_test"


config_set = {
	"development": DevelopmentConfig,
	"testing": TestingConfig,
	"production": ProductionConfig
}

