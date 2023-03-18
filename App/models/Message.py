from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from datetime import datetime

class Message(db.Model):
    messageID = db.Column(db.Integer, primary_key=True)
    text= db.Column(db.String(120))
    date= db.Column(db.DateTime, default=datetime.utcnow())
    senderID = db.Column(db.Integer, db.ForeignKey('user.userId'))
    chatID = db.Column(db.Integer, db.ForeignKey('chat.ChatID'))
    notifications = db.relationship('Notification', backref='message', lazy=True)

    def __init__(self, text, senderID, chatID, date=datetime.utcnow()):
        self.text = text
        self.date = date
        self.senderID = senderID
        self.chatID = chatID

    def toJSON(self):
        return{
            'messageID':  self.messageID,
            'text': self.text,
            'date': self.date.isoformat(),
            'senderID': self.senderID,
            'chatID': self.chatID,
            'notifications': [notification.toJSON() for notification in self.notifications]
        }