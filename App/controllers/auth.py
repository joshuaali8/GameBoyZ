import flask_login
import re
from flask_jwt import JWT
from App.models import User


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

#check for valid email
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@my.uwi.edu$"
    return re.match(pattern, email) is not None

#check for valid id
def is_valid_id(id):
    # Check that the ID is a 9-digit number
    pattern = r"^\d{9}$"
    return re.match(pattern, id) is not None

"""
# Example usage
email = "joshua.ali@my.uwi.edu"
id = "816023462"
if is_valid_email(email) and is_valid_id(id):
    # Check if the ID is a valid ID (e.g. exists in a database)
    # and if the email is not already associated with another account
    # You can implement this part of the authentication using a database or other storage mechanism.
    # Return True if the authentication is successful.
    print("Authentication successful!")
else:
    print("Invalid email or ID.")

"""
# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return User.query.get(payload['identity'])

def login_user(user, remember):
    return flask_login.login_user(user, remember=remember)


def logout_user():
    flask_login.logout_user()

def setup_jwt(app):
    return JWT(app, authenticate, identity)