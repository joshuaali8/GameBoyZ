from flask import flask
from flask_sqlalchemy import SQLAlchemy

class CETLAdmin (db.Model):
    CETLAdminID = db.Column(db.Integer, primary_key=True)

    def __init__(self , CETLAdminID):
        self.CETLAdminID= (CETLAdminID)

 def toJSON(self):
        return{
            'CETLAdminID': self.CETLAdminID
        }

