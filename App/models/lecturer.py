from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models.User import User

class Lecturer(User):
    __tablename__ = 'lecturer'
    __mapper_args__ = {
        'polymorphic_identity': 'lecturer',
    }
    
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)
    lecturerID = db.Column(db.Integer, primary_key=True)

    # add unique constraint to userId
    __table_args__ = (
        db.UniqueConstraint('userId'),
    )

    def __init__(self, firstname, lastname, password, lecturerID):
            super().__init__(firstname, lastname, password, roleID=3)
            self.lecturerID = lecturerID
            
            
    def toJSON(self):
            data = super().toJSON()
            data['lecturerID'] = self.lecturerID
            return data