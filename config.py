import os

class MainConfig():
	"""Configuration class"""
	DEBUG = False
	TESTING = False
	SECRET_KEY = "andela"
	DB_URL = "postgresql://sendit_admin:password@localhost/sendit_db"


class DevelopmentConfig(MainConfig):
	"""Development configuration"""
	DEBUG = True


class ProductionConfig(MainConfig):
	"""Production configuration"""
	DB_URL = os.getenv('DB_URL')
	SECRET_KEY = os.getenv('SECRET_KEY')


class TestingConfig(MainConfig):
	DEBUG = True
	DB_URL = "postgresql://sendit_admin:password@localhost/sendit_test"


config_set = {
	"development": DevelopmentConfig,
	"testing": TestingConfig,
	"production": ProductionConfig
}

