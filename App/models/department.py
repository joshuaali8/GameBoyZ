from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Department(db.Model):
    departmentID = db.Column(db.Integer, primary_key=True)
    departmentName = db.Column(db.String(200))
    facultyID = db.Column(db.Integer, forgein_key= True)
    programmeID = db.Column(db.Integer, forgein_key = True)
    
    def __init__(self , departmentID, departmentName, facultyID, programmeID):
            self.departmentID =(departmentID)
            self.departmentName = (departmentName)
            self.facultyID = (facultyID)
            self.programmeID =(programmeID)
            
    def toJSON(self):
            return{
                'departmentID': self.departmentID,
                'departmentName': self.departmentName, 
                'facultyID': self.facultyID,
                'programmeID': self.programmeID
                
                
            }