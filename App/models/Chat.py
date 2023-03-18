from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from datetime import datetime


class Chat(db.Model):
    ChatID = db.Column(db.Integer, primary_key=True)
    messages= db.relationship('Message', backref='chat', lazy=True)
    chatTime= db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship('User', secondary='chat_users')
    accessControl = db.relationship('AccessControl', backref='chat', lazy=True)

    def __init__(self, messages, users, chatTime=datetime.utcnow()):
        self.messages=messages
        self.chatTime=chatTime
        self.users=users

    def toJSON(self):
        return{
            'ChatID': self.ChatID,
            'messages': [message.toJSON() for message in self.messages],
            'chatTime': self.chatTime.isoformat(),
            'users': [user.toJSON() for user in self.users],
            'accessControl': [access.toJSON() for access in self.accessControl]
        }
