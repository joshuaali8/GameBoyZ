from flask import flask
from flask_sqlalchemy import SQLAlchemy

class Date(db.Model):
    Day = db.Column(db.Integer)
    Month= db.Column(db.Integer)
    Year= db.Column(db.Integer)
    Time= db.Column(db.Integer)

    def __init__(self , Day, Month, Year, Time)
        self.Day =(Day)
        self.Month = (Month)
        self.Year = (Year)
        self.Time =(Time)
        
 def toJSON(self):
        return{
            ' Day': self.Day
            'Month': self.Month
            'Year'= self.Year
            'Time'=  self.Time
            
            
        }