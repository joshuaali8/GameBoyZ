from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_course(courseCode, courseTitle, facultyID, programmeID, departmentID):
    newcourse= Course(courseCode=courseCode, courseTitle=courseTitle, facultyID=facultyID, programmeID=programmeID, departmentID=departmentID)
    db.session.add(newcourse)
    db.session.commit()
    return newcourse

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_course_by_courseCode(courseCode):
    return Course.query.get(courseCode)


def get_course_by_courseTitle(courseTitle):
    return Course.query.get(courseTitle)

def get_course_by_facultyID(facultyID):
    return Course.query.get(facultyID)

def get_course_by_programmeID(programmeID):
    return Course.query.get(programmeID)

def get_course_by_departmentID(departmentID):
    return Course.query.get(departmentID)

def get_all_courses():
    return Course.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_course (courseCode, courseTitle, facultyID, programmeID, departmentID):
    updatedcourse = get_course_by_courseCode(courseCode)
    if updatedcourse:
        updatedcourse.courseTitle = courseTitle
        updatedcourse.facultyID = facultyID
        updatedcourse.programmeID = programmeID
        updatedcourse.departmentID = departmentID
        db.session.add(updatedcourse)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_course(courseCode):
    delcourse = get_course_by_courseCode(courseCode)
    if delcourse:
        db.session.delete(delcourse)
        return db.session.commit()
    return None


"""--------------------------------------- """