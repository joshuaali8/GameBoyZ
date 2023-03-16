from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.database import db

class Message(db.Model):
    messageID = db.Column(db.Integer, primary_key=True)
    text= db.Column(db.String(120))
    #Date= db.Column(db.DateTime)
    #Sender= db.Column(db.User)

    def __init__(self , messageID, text, Date, Sender):
            self.messageID =(messageID)
            self.text= (text)
            self.Date = (Date)
            self.Sender =(Sender)
            
    def toJSON(self):
            return{
                'messageID':  self.messageID,
                'text': self.text,
                'Date': self.Date,
                'Sender': self.Sender
                
                
            }