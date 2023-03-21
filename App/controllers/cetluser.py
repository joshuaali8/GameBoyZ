from App.models import *
from App.database import db

"""GET FUNCTIONS """
"""--------------------------------------- """

def get_cetluser_by_email(email):
    return CETLUser.query.filter_by(email=email).first()

def get_cetluser(CETLUserID):
    return CETLUserID.query.get(CETLUserID)

# Get a lecturer using a specific Id
# Return the lecturer in json format or None otherwise
def get_cetluser_toJSON(CETLUserID):
    user = get_cetluser(CETLUserID)
    if user:
        return user.toJSON
    return None

def get_all_cetluser():
    return CETLUser.query.all()

def get_all_cetluser_json():
    users = CETLUser.query.all()
    if not users:
        return []
    cetluser = [users.toJSON() for users in users]
    return users

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """
def update_cetluser(firstname, lastname, password, CETLUserID):
    cetluser = get_cetluser(CETLUserID)
    if cetluser:
        cetluser.firstname = firstname
        cetluser.lastname = lastname
        cetluser.email = email
        db.session.add(cetladmin)
        return db.session.commit()
    return None

"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """
def delete_cetluser(CETLUserID):
    cetluser = get_cetluser(CETLUserID)
    if cetluser:
        db.session.delete(cetluser)
        return db.session.commit()
    return None

"""--------------------------------------- """

""" UWI COMA FUNCTIONS """
"""--------------------------------------- """

"""--------------------------------------- """