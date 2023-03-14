from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Resoruce(db.Model):
    resourceID = db.Column(db.Integer, primary_key=True)
    resourceTag= db.Column(db.String(20))
    resourcesDate=db.Column(db.Blob)
    resourceName= db.Column(db.String(100))

    def __init__(self , resourceID, resourceTag, resourcesDate, resourceName):
            self.resourceID =(resourceID)
            self.resourceTag = (resourceTag)
            self.resourcesDate = (resourcesDate)
            self.resourceName = (resourceName)
            
            
    def toJSON(self):
            return{
                'resourceID': self.resourceID,
                'resourceTag': self.resourceTag,
                'resourcesDate': self.resourcesDate,
                'resourceName': self.resourceName    
            }