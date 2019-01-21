import os

class MainConfig():
	"""Configuration class"""
	DEBUG = False
	TESTING = False
	SECRET_KEY = "andela"
	DBNAME = "sendit_db"
	DBUSER = "sendit_admin"
	DBHOST = "localhost"
	DBPASS = "andela"


class DevelopmentConfig(MainConfig):
	"""Development configuration"""
	DEBUG = True
	DB_URL = "postgresql://sendit_admin:password@localhost/sendit_db"


class ProductionConfig(MainConfig):
	"""Production configuration"""
	DB_URL = "postgres://lcymvirjcnsqmd:f287c244235d44517383dbb35ac2a0ee187b5b951b18de6d53bc720b003076cc@ec2-54-225-89-195.compute-1.amazonaws.com:5432/d4lvgiuliifvth"
	SECRET_KEY = os.getenv('SECRET_KEY')


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

