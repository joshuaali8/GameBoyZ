from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Lecturer(db.Model):
    lecturerID = db.Column(db.Integer, primary_key=True)

    def __init__(self , lecturerID):
            self.lecturerID =(lecturerID)
            
            
    def toJSON(self):
            return{
                'lecturerID': self.lecturerID          
            }