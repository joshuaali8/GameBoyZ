from flask import flask
from flask_sqlalchemy import SQLAlchemy

class CETLUserQueue(db.Model):
    CETLUserQ = db.Column(db.Integer, primary_key=True)
    CETLUserID = db.Column(db.Integer, forgein_key=True)
    numofCourses = db.Column(db.Integer)
    positionInUserQueue = db.Column(db.Integer)
    changes = db.Column(db.Enum)
    approveCourses= db.Column(db.Boolean)

 def __init__(self , CETLUserQ, CETLUserID, numofCourses, positionInUserQueue, changes, approveCourses):
        self.CETLUserQ= (CETLUserQ)
        self.CETLUserID=(CETLUserID)
        self.numofCourses= (numofCourses)
        self.positionInUserQueue= (positionInUserQueue)
        self.changes=(changes)
        self.approveCourses=(approveCourses)

 def toJSON(self):
        return{
            'CETLUserQ': self.CETLUserQ,
            'CETLUserID': self.CETLUserID,
            'numofCourses': self.numofCourses,
            'positionInUserQueue': self.positionInUserQueue,
            'changes': self.changes,
            'approveCourses': self.approveCourses
        }

