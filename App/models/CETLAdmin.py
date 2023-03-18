from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models.user import User

#make user class abstract and reference into cetladmin
class CETLAdmin (User):
    #CETLAdminID = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'cetl_admin'
    __mapper_args__ = {
        'polymorphic_identity': 'cetladmin',
    }

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)
    CETLAdminID = db.Column(db.Integer, primary_key = True)

    # add unique constraint to userId
    __table_args__ = (
        db.UniqueConstraint('userId'),
    )

    def __init__(self, firstname, lastname, password, CETLAdminID):
            super().__init__(firstname, lastname, password, roleID=1)
            self.CETLAdminID = CETLAdminID
            #self.CETLAdminID= (CETLAdminID)

    def toJSON(self):
            #return{
             #   'CETLAdminID': self.CETLAdminID
            #}
            data = super().toJSON()
            data['CETLAdminID'] = self.CETLAdminID
            return data

