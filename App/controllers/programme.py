from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_programme(programmeID, programmeName, departmentID, programmeLevel):
    newprogramme= Programme (programmeID= programmeID, programmeName= programmeName, departmentID= departmentID, programmeLevel= programmeLevel)
    db.session.add(newprogramme)
    db.session.commit()
    return newprogramme

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_programme_byID(programmeID):
    return Programme.query.get(programmeID)


def get_programme_by_programmeName(programmeName):
    return Programme.query.get(programmeName)


def get_programme_by_programmeLevel(programmeLevel):
    return Programme.query.get(programmeLevel)


def get_all_programmes():
    return Programme.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_programme(programmeID, programmeName, departmentID, programmeLevel):
    updatedprogramme = get_programme_byID(programmeID)
    if updatedprogramme:
        updatedprogramme.programmeName = programmeName
        updatedprogramme.departmentID = departmentID
        updatedprogramme.programmeLevel = programmeLevel
        db.session.add(updatedprogramme)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_programme(programmeID):
    delprogramme = get_programme_byID(programmeID)
    if delprogramme:
        db.session.delete(delprogramme)
        return db.session.commit()
    return None


"""--------------------------------------- """