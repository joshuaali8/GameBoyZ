from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Programme(db.Model):
    programmeID = db.Column(db.Integer, primary_key=True)
    programmeName = db.Column(db.String(200))
    departmentID = db.Column(db.Integer, db.ForeignKey('department.departmentID'))
    programmeLevel = db.Column(db.String(10))

    def __init__(self, programmeID, programmeName, departmentID, programmeLevel):
        self.programmeID = programmeID
        self.programmeName = programmeName
        self.departmentID = departmentID
        self.programmeLevel = programmeLevel

    def toJSON(self):
        return {
            'programmeID': self.programmeID,
            'programmeName': self.programmeName,
            'departmentID': self.departmentID,
            'programmeLevel': self.programmeLevel,
        }
