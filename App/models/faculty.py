from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Faculty(db.Model):
    facultyID = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String(200))
    departmentID =db.Column(db.Integer, db.ForeignKey('Department.departmentID'))

    def __init__(self , facultyID, facultyName, departmentID):
            self.facultyID =(facultyID)
            self.facultyName = (facultyName)
            self.departmentID = (departmentID)
            
            
    def toJSON(self):
            return{
                'facultyID':  self.facultyID ,
                'facultyName': self.facultyName,
                'departmentID': self.departmentID   
                
            }