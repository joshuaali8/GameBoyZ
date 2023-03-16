from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Queue(db.Model):
    queueID = db.Column(db.Integer, primary_key=True)
    documentID = db.Column(db.Integer, db.ForeignKey('Document.documentID'))
    position = db.Column(db.Integer)
    dateSubmitted= db.Column(db.DateTime)
    estimatedResponseTime =db.Column(db.Integer)
    assignedCetl =db.Column(db.Boolean)
    
    def __init__(self , queueID, documentID, position, dateSubmitted, estimatedResponseTime, assignedCetl):
            self.queueID =(queueID)
            self.documentID = (documentID)
            self.position = (position)
            self.dateSubmitted = (dateSubmitted)
            self.estimatedResponseTime = (estimatedResponseTime)
            self.assignedCetl = (assignedCetl)

            
    def toJSON(self):
            return{
                'queueID':  sself.queueID,
                'documentID':  self.documentID,
                'position': self.position ,
                'dateSubmitted': self.dateSubmitted,
                'estimatedResponseTime': self.estimatedResponseTime ,
                'assignedCetl': self.assignedCetl  
                
            }