from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Chat(db.Model):
    ChatID = db.Column(db.Integer, primary_key=True)
    messages= db.Column(db.String)
    chatTime= db.Column(db.String)
    senderID =db.Column(db.Integer)
    documentID = db.Column(db.Integer)
    receiverID= db.Column(db.Integer)

    def __init__(self , ChatID, messages,chatTime, senderID,documentID,receiverID):
            self.ChatID= (ChatID)
            self.messages=(messages)
            self.chatTime = (chatTime)
            self.senderID= (senderID)
            self.documentID =(documentID)
            self.receiverID =(receiverID)

    def toJSON(self):
            return{
                'ChatID': self.ChatID,
                'messages': self.messages,
                'chatTime': self.chatTime,
                'senderID': self.senderID,
                'documentID': self.documentID,
                'receiverID': self.receiverID
            }
