import os


class BaseConfig(object):
    DEBUG = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/db.sqlite'


class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://augczxupdfanck:c1e4912663560b6455696d48b64203742e425aec46219b218806d5a54a48e911@ec2-54-217-234-157.eu-west-1.compute.amazonaws.com:5432/d3hop2juio20u6'


class HerokuConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
