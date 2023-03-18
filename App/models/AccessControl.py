from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class AccessControl(db.Model):
    __tablename__ = 'access_control'
    
    accessID = db.Column(db.Integer, primary_key=True)
    chatID = db.Column(db.Integer, db.ForeignKey('chat.ChatID'))
    userID = db.Column(db.Integer, db.ForeignKey('user.userId'))
    granted = db.Column(db.Boolean, nullable=False, default=False)
    
    user = db.relationship('User', backref='access_controls')
    chat = db.relationship('Chat', backref='access_controls')
    
    def __init__(self, chatID, userID, granted=False):
        self.chatID = chatID
        self.userID = userID
        self.granted = granted
        
    def to_json(self):
        return {
            'accessID': self.accessID,
            'chatID': self.chatID,
            'userID': self.userID,
            'granted': self.granted
        }