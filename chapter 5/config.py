class Config(object):
 pass


class ProdConfig(Config):
 pass


class DevConfig(Config):
 DEBUG = True
 SECRET_KEY='#yaseen123'

 SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
 SQLALCHEMY_TRACK_MODIFICATIONS = False