from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Date(db.Model):
    DateID = db.Column(db.Integer, primary_key=True)
    Day = db.Column(db.Integer)
    Month= db.Column(db.Integer)
    Year= db.Column(db.Integer)
    Time= db.Column(db.Integer)

    def __init__(self , DateID, Day, Month, Year, Time):
            self.DateID= (DateID)
            self.Day =(Day)
            self.Month = (Month)
            self.Year = (Year)
            self.Time =(Time)
            
    def toJSON(self):
        return{
            'Day': self.Day,
            'Month': self.Month,
            'Year': self.Year,
            'Time': self.Time
            
            
        }