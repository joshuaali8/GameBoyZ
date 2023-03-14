from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db


class Document(db.Model):
    documentID = db.Column(db.Integer, primary_key=True)
    resourceID= db.Column(db.Integer, forgein_key=True)
    queueID= db.Column(db.Integer)
    lecturerID= db.Column(db.Integer)
    CETLUserID= db.Column(db.Integer)
    facultyID= db.Column(db.Integer)
    facultyName= db.Column(db.Integer)
    programmeName= db.Column(db.Integer)
    courseCode= db.Column(db.String(40))
    documentName= db.Column(db.String(120))
    documentType= db.Column(db.String(120))
    State= db.Column(db.Enum)
    Level= db.Column(db.String)
    dueDate= db.Column(db.DateTime)


    def __init__(self, documentID, resourceID, queueID, lecturerID, CETLUserID, facultyID, facultyName, programmeName, courseCode, documentName, documentType, State, Level, dueDate):
            self.documentID =(documentID)
            self.resourceID = (resourceID)
            self.queueID = (queueID)
            self.lecturerID =(lecturerID)
            self.CETLUserID =(CETLUserID)
            self.facultyID =(facultyID)
            self.facultyName =(facultyName)
            self.programmeName = (programmeName)
            self.courseCode = (courseCode)
            self.documentName = (documentName)
            self.documentType = (documentType)
            self. State = (State)
            self.Level = ( Level)
            self.dueDate = (dueDate)

            
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
                'State':  self. State,
                'Level': self.Level,
                'dueDate': self.dueDate
    
            }