import os

"""
In the previous lesson when we referred to the database connection the line of code was similar to this:
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://db_dev:123456@localhost:5432/trello_clone_db"
Realise that this variable is configuring the flask application, same with the secret key. In this new modular
structure we will create a separate config.py file to set these variables. 
"""

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Access to .env and get the value of SECRET_KEY, the variable name can be any but needs to match.
    JWT_SECRET_KEY =  os.environ.get("SECRET_KEY")
    JSON_SORT_KEYS=False # Puts columns in right order instead of alphabetically (in schema added ordered = True)
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # Access to .env and get the value of DATABASE_URL, the variable name can be any but needs to match.
        value = os.environ.get("DATABASE_URL")

        if not value:
            raise ValueError("DATABASE_URL is not set")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()