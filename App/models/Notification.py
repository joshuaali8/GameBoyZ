from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from datetime import datetime

class Notification(db.Model):
    notificationID = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))
    date = db.Column(db.DateTime, default=datetime.utcnow())
    userID = db.Column(db.Integer, db.ForeignKey('user.userId'))
    messageID = db.Column(db.Integer, db.ForeignKey('message.messageID'))

    def __init__(self, text, userID, messageID, date=datetime.utcnow()):
        self.text = text
        self.date = date
        self.userID = userID
        self.messageID = messageID

    def toJSON(self):
        return{
            'notificationID': self.notificationID,
            'text': self.text,
            'date': self.date.isoformat(),
            'userID': self.userID,
            'messageID': self.messageID
        }