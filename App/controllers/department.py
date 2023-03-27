from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_department (departmentID, departmentName, facultyID, programmeID):
    newdepartment= Department(departmentID=departmentID, departmentName=departmentName, facultyID=facultyID, programmeID= programmeID)
    db.session.add(newdepartment)
    db.session.commit()
    return newdepartment

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_department_byID(departmentID):
    return Department.query.get(departmentID)


def get_department_by_departmentName(departmentName):
    return Department.query.get(departmentName)


def get_all_department():
    return Department.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_department(departmentID, departmentName, facultyID, programmeID):
    updateddepartment = get_department_byID(departmentID)
    if updateddepartment:
        updateddepartment.departmentName = departmentName
        updateddepartment.facultyID = facultyID
        updateddepartment.programmeID = programmeID
        db.session.add(updateddepartment)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_department(departmentID):
    deldepartment = get_department_byID(departmentID)
    if deldepartment:
        db.session.delete(deldpartment)
        return db.session.commit()
    return None


"""--------------------------------------- """