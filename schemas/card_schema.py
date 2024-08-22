from main import ma
from marshmallow import fields

# create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CardSchema(ma.Schema):
    class Meta:
        # To show the columns in the right order as defined in our schema, also add JSON_SORT_KEYS=False in the config.py
        ordered = True
        # Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority", "user")
    # nested property to add more about the user to card - import fields from marshmallow to do this.
    # As we don't want to add all the users info (ie passwords etc), we can select 'only' what fields we want, here: "email".
    user = fields.Nested("UserSchema", only=("email",)) # add comma at end.

# single card schema, when one card needs to be retrieved
card_schema = CardSchema()
# multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)