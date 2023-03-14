from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Programmme(db.Model):
   programmeID = db.Column(db.Integer, primary_key=True)
   programmeName = db.Column(db.String(200))
   departmentID = db.Column(db.Integer, forgein_key=True)
   programmeLevel =db.Column(db.String(10))

   def __init__(self , facultyID, facultyName, departmentID, programmeLevel):
        self.facultyID = (facultyID)
        self.facultyName = (facultyName)
        self.departmentID = (departmentID)
        self.programmeLevel = (programmeLevel)
              
              
   def toJSON(self):
        return{
                'facultyID':  self.facultyID ,
                'facultyName': self.facultyName,
                'departmentID': self.departmentID ,  
                'programmeLevel': self.programmeLevel 
                  
              }