from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models.user import User


class CETLUser(db.Model):
    __tablename__ = 'cetl_user'
    __mapper_args__ = {
        'polymorphic_identity': 'cetluser',
    }

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)
    CETLUserID= db.Column(db.Integer, primary_key=True)

    # add unique constraint to userId
    __table_args__ = (
        db.UniqueConstraint('userId'),
    )

    def __init__(self, firstname, lastname, password, CETLUserID):
            super().__init__(firstname, lastname, password, roleID=2)
            self.CETLUserID = CETLUserID

    def toJSON(self):
            data = super().toJSON()
            data['CETLUserID'] = self.CETLUserID
            return data