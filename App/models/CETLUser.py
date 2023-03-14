from flask import flask
from flask_sqlalchemy import SQLAlchemy

class CETLUser(db.Model):
    CETLUserID = db.Column(db.Integer, primary_key=True)


 def __init__(self , CETLUserID):
        self.CETLUserID= (CETLUserID)

 def toJSON(self):
        return{
            'CETLUserID': self.CETLUserID
        }