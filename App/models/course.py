from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db


class Course(db.Model):
    courseCode = db.Column(db.Integer, primary_key=True)
    courseTitle = db.Column(db.String(120))
    facultyID = db.Column(db.Integer, db.ForeignKey('faculty.facultyID'))
    programmeID = db.Column(db.Integer, db.ForeignKey('programme.programmeID'))
    departmentID = db.Column(db.Integer, db.ForeignKey('department.departmentID'))

    def __init__(self, courseCode, courseTitle, facultyID, programmeID, departmentID):
        self.courseCode = courseCode
        self.courseTitle = courseTitle
        self.facultyID = facultyID
        self.programmeID = programmeID
        self.departmentID = departmentID

    def toJSON(self):
        return {
            'courseCode': self.courseCode,
            'courseTitle': self.courseTitle,
            'facultyID': self.facultyID,
            'programmeID': self.programmeID,
            'departmentID': self.departmentID,
        }
