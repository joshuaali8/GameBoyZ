from flask import flask
from flask_sqlalchemy import SQLAlchemy

class Resoruce(db.Model):
    resourceID = db.Column(db.Integer, primary_key=True)
    resourceTag= db.Column(db.String(20))
    resourcesDate=
    resourceName= db.Column(db.String(100))

 def __init__(self , resourceID, resourceTag, resourcesDate, resourceName)
        self.resourceID =(resourceID)
        self.resourceTag = (resourceTag)
        self.resourcesDate = (resourcesDate)
        self.resourceName = (resourceName)
        
        
 def toJSON(self):
        return{
            'resourceID': self.resourceID
            'resourceTag': self.resourceTag
            'resourcesDate'= self.resourcesDate  
            'resourceName'= self.resourceName    
        }