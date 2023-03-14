from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class submittedProposals(db.Model):
    submittedID = db.Column(db.Integer, primary_key=True)
    lecturerID= db.Column(db.Integer, forgein_key-True)
    documentID= db.Column(db.Integer, forgein_key=True)
    dateSubmitted= db.Column(db.DateTime)
    responseStatus= db.Column(db.Boolean)
    assignedCetl= db.Column(db.Boolean)
    CETLUserID= db.Column(db.Integer)

    def __init__(self , submittedID, lecturerID, documentID, dateSubmitted, responseStatus, assignedCetl, CETLUserID):
            self.submittedID =(submittedID)
            self.lecturerID = (lecturerID)
            self.documentID = (documentID)
            self.dateSubmitted = (dateSubmitted)
            self.responseStatus= (responseStatus)
            self.assignedCetl = (assignedCetl)
            self.CETLUserID = (CETLUserID)
            
            
    def toJSON(self):
            return{
                'submittedID':  self.submittedID,
                'lecturerID':  self.lecturerID, 
                'documentID': self.lecturerID,
                'dateSubmitted': self.documentID,
                'dateSubmitted': self.dateSubmitted,
                'responseStatus': self.responseStatus,
                'assignedCetl': self.assignedCetl,
                'CETLUserID': self.CETLUserID    
                
            }