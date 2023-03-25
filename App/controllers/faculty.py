from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_faculty(facultyID, facultyName, departmentID):
    newfaculty= Faculty (facultyID= facultyID, facultyName= facultyName, departmentID= departmentID)
    db.session.add(newfaculty)
    db.session.commit()
    return newfaculty

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_faculty_byID(facultyID):
    return Faculty.query.get(facultyID)


def get_faculty_by_facultyName(facultyName):
    return Faculty.query.get(facultyName)


def get_all_faculty():
    return Faculty.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_faculty(facultyID, facultyName, departmentID):
    updatedfaculty = get_faculty_byID(facultyID)
    if updatedfaculty:
        updatedfaculty.facultyName = facultyName
        updatedfaculty.departmentID = departmentID
        db.session.add(updatedfaculty)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_faculty(facultyID):
    delfaculty = get_faculty_byID(facultyID)
    if delfaculty:
        db.session.delete(delfaculty)
        return db.session.commit()
    return None


"""--------------------------------------- """