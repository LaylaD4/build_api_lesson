# We need to import our new controllers and apply those blueprints to our app.

from controllers.cards_controller import cards
from controllers.auth_controller import auth

# Now we can just import the registerable_controllers list into our create_app function, 
# and when we add more controllers, adding them to the list here will make sure they're included!
registerable_controllers = [
    auth,
    cards
]

