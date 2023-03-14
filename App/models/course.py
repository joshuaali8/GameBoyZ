from flask import flask
from flask_sqlalchemy import SQLAlchemy


class Course (db.Model):
    courseCode = db.Column(db.Integer, primary_key=True)
    courseTitle= db.Column(db.String(120))
    facultyID = db.Column(db.Integer , forgein_key=True)
    programmeID = db.Column(db.Integer, forgein_key= True)
    departmentID = db.Column(db.Integer, forgein_key=True)

 def __init__(self , courseCode, courseTitle, facultyID , programmeID , departmentID)
        self.courseCode =(courseCode)
        self.courseTitle = (courseTitle)
        self.facultyID = (facultyID)
        self.programmeID =(programmeID)
        self.departmentID =(departmentID)

 def toJSON(self):
        return{
            'courseCode': self.courseCode
            'courseTitle':  self.courseTitle
            'facultyID'= self.facultyID
            'programmeID'=  self.programmeID
            'departmentID'= self.departmentID
            
        }