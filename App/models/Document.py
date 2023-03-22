from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db


class Document(db.Model):
    documentID = db.Column(db.Integer, primary_key=True)
    resourceID = db.Column(db.Integer, db.ForeignKey('resources.resourceID'))
    queueID = db.Column(db.Integer, db.ForeignKey('queue.queueID'))
    lecturerID= db.Column(db.Integer, db.ForeignKey('lecturer.lecturerID'))
    CETLUserID= db.Column(db.Integer, db.ForeignKey('cetl_user.CETLUserID'))
    facultyID= db.Column(db.Integer, db.ForeignKey('faculty.facultyID'))
    facultyName= db.Column(db.String)
    programmeName= db.Column(db.String)
    courseCode= db.Column(db.String(10), db.ForeignKey('course.courseCode'))
    courseTitle = db.Column(db.String(120))
    documentName= db.Column(db.String(120))
    documentType= db.Column(db.String(120))
    document = db.Column(db.LargeBinary)
    State= db.Column(db.Enum('submitted', 'assigned', 'approved', 'amend', name='document_state'))
    Level= db.Column(db.String)
    dueDate= db.Column(db.DateTime)


    def __init__(self, documentID, resourceID, queueID, lecturerID, CETLUserID, facultyID, facultyName, programmeName, courseCode, documentName, documentType, document, State, Level, dueDate):
            self.documentID =documentID
            self.resourceID = resourceID
            self.queueID = queueID
            self.lecturerID =lecturerID
            self.CETLUserID = CETLUserID
            self.facultyID =facultyID
            self.facultyName =facultyName
            self.programmeName = programmeName
            self.courseCode = courseCode
            self.documentName = documentName
            self.documentType = documentType
            self.document = document
            self. State = State
            self.Level = Level
            self.dueDate = dueDate

            
    def toJSON(self):
            return{
                'documentID': self.documentID ,
                'resourceID': self.resourceID,
                'queueID': self.queueID,
                'lecturerID': self.lecturerID,
                'CETLUserID': self.CETLUserID,
                'facultyID':  self.facultyID,
                'facultyName': self.facultyName,
                'programmeName': self.programmeName,
                'courseCode':  self.courseCode,
                'documentName': self.documentName,
                'documentType': self.documentType,
                'document': self.document,
                'State':  self.State,
                'Level': self.Level,
                'dueDate': self.dueDate
    
            }