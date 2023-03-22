from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Resource(db.Model):
    resourceID = db.Column(db.Integer, primary_key=True)
    resourceTag= db.Column(db.String(20))
    resourceData = db.Column(db.LargeBinary)
    resourceName= db.Column(db.String(100))

    def __init__(self , resourceID, resourceTag, resourceData, resourceName):
            self.resourceID =resourceID
            self.resourceTag = resourceTag
            self.resourcesData = resourceData
            self.resourceName = resourceName
            
            
    def toJSON(self):
            return{
                'resourceID': self.resourceID,
                'resourceTag': self.resourceTag,
                'resourceData': self.resourceData,
                'resourceName': self.resourceName    
            }