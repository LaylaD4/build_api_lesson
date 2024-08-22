from main import ma
from marshmallow.validate import Length
from models.users import User
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        # To show the columns in the right order as defined in our schema, also add JSON_SORT_KEYS=False in the config.py
        ordered = True
        # We added cards to the list of fields (two way nesting)
        fields = ['id', 'email', 'password', 'admin', 'cards']
        # We only want to load these attributes when a user signs up, 
        # now when we invoke 'dump' to retrieve the users data they will not show up.
        load_only = ['password', 'admin']
    # Set the passwords length to a minimum of 6 characters.
    password = ma.String(validate=Length(min=6))
    # set cards as a field that will store a list. Exclude user from CardSchema to avoid infinite loop of calls between users and cards.
    cards = fields.List(fields.Nested("CardSchema", exclude=("user",))) 

user_schema = UserSchema()
users_schema = UserSchema(many=True)