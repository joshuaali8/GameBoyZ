from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db


#make user class abstract and reference into cetladmin
class CETLAdmin (db.Model):
    CETLAdminID = db.Column(db.Integer, primary_key=True)

    def __init__(self , CETLAdminID):
            self.CETLAdminID= (CETLAdminID)

    def toJSON(self):
            return{
                'CETLAdminID': self.CETLAdminID
            }

