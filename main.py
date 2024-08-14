from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # creating our database object! This allows us to use our ORM (me: must import it into models files.)
    # not using this anymore as we need to import the model to the main file that will return a double dependency error.
    # db = SQLAlchemy(app) 
    # Here we are creating a generic db object that we can import into our model's code, and then waiting until 
    # the create_app function is called to associate that db object with our app.
    db.init_app(app)

    # creating our marshmallow object! This allows us to use schemas
    ma.init_app(app)

    #creating the jwt and bcrypt objects! this allows us to use authentication
    bcrypt.init_app(app)
    jwt.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    # import the controllers and activate the blueprints (in controllers/__init__.py)
    from controllers import registerable_controllers

    # The registerable_controllers is a list in controllers/__init__.py
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app
