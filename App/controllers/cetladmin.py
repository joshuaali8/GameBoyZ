from App.models import *
from App.database import db

"""GET FUNCTIONS """
"""--------------------------------------- """

def get_cetladmin_by_email(email):
    return CETLAdmin.query.filter_by(email=email).first()

def get_cetladmin(CETLAdminID):
    return CETLAdmin.query.get(CETLAdminID)

# Get a lecturer using a specific Id
# Return the lecturer in json format or None otherwise
def get_cetladmin_toJSON(CETLAdminID):
    admin = get_cetladmin(CETLAdminID)
    if admin:
        return admin.toJSON
    return None

def get_all_cetladmin():
    return CETLAdmin.query.all()

def get_all_cetladmin_json():
    admins = CETLAdmin.query.all()
    if not admins:
        return []
    admins = [admin.toJSON() for admin in admins]
    return admins

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """
def update_cetladmin(CETLAdminID, firstname, lastname, email):
    cetladmin = get_cetladmin(CETLAdminID)
    if cetladmin:
        cetladmin.firstname = firstname
        cetladmin.lastname = lastname
        cetladmin.email = email
        db.session.add(cetladmin)
        return db.session.commit()
    return None

"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """
def delete_cetladmin(CETLAdminID):
    cetladmin = get_cetladmin(CETLAdminID)
    if cetladmin:
        db.session.delete(cetladmin)
        return db.session.commit()
    return None

"""--------------------------------------- """

""" UWI COMA FUNCTIONS """
"""--------------------------------------- """

"""--------------------------------------- """