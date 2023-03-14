from flask import flask
from flask_sqlalchemy import SQLAlchemy

class Lecturer(db.Model):
    lecturerID = db.Column(db.Integer, primary_key=True)

 def __init__(self , lecturerID)
        self.lecturerID =(lecturerID)
        
        
 def toJSON(self):
        return{
            'lecturerID': self.lecturerID          
        }