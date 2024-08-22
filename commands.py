from main import db
from flask import Blueprint
from main import bcrypt
from models.cards import Card
from models.users import User
from datetime import date

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("seed")
def seed_db():

    # Create the users first and commit the changes as user needs to be created before the card, as it needs the user id in the card model.
    admin_user = User(
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        admin = True
    )
    db.session.add(admin_user)

    user1 = User(
        email = "user1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user1)
    # This extra commit will end the transaction and generate the ids for the user. 
    # Commit changes between the creation of the users and cards. That way the user 
    # object will have its id available to add it to the card. Without this extra commit user's id is None.
    db.session.commit()

    # create the card object
    card1 = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title = "Start the project",
        description = "Stage 1, creating the database",
        status = "Done",
        priority = "High",
        date = date.today(),
        user_id = user1.id # Or can be done this way: user = user1
    )
    # Add the object as a new row to the table
    db.session.add(card1)

    card2 = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title = "SQLAlchemy and Marshmallow",
        description = "Stage 2, integrate both modules in the project",
        status = "Ongoing",
        priority = "High",
        date = date.today(),
        user = user1 # Or can be done: user_id = user1.id
    )
    # Add the object as a new row to the table
    db.session.add(card2)

    # commit the changes
    db.session.commit()
    print("Table seeded") 

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 