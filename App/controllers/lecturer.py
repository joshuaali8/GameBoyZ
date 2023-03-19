from App.models import *
from App.database import db

"""GET FUNCTIONS """
"""--------------------------------------- """

def get_lecturer_by_email(email):
    return Lecturer.query.filter_by(email=email).first()

def get_lecturer(lecturerID):
    return Lecturer.query.get(lecturerID)

# Get a lecturer using a specific Id
# Return the lecturer in json format or None otherwise
def getLecturer_toJSON(lecturerID):
    lecturer = get_lecturer(lecturerID)
    if lecturer:
        return lecturer.toJSON
    return None

def get_all_lecturers():
    return Lecturer.query.all()

def get_all_lecturers_json():
    lecturers = Lecturer.query.all()
    if not lecturers:
        return []
    lecturers = [lecturer.toJSON() for lecturer in lecturers]
    return lecturers

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """
def update_lecturer(lecturerID, firstname, lastname, email):
    lecturer = get_lecturer(lecturerID)
    if lecturer:
        lecturer.firstname = firstname
        lecturer.lastname = lastname
        lecturer.email = email
        db.session.add(lecturer)
        return db.session.commit()
    return None

"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """
def delete_lecturer(lecturerID):
    lecturer = get_lecturer(lecturerID)
    if lecturer:
        db.session.delete(lecturer)
        return db.session.commit()
    return None

"""--------------------------------------- """

""" UWI COMA FUNCTIONS """
"""--------------------------------------- """
def uploadProposal():

    return 
"""--------------------------------------- """