from App.models import *
from App.database import db
from datetime import datetime
 
def create_message(messageID, text, senderID, chatID, date=datetime.utcnow()):
    newmessage= Message(text= text, senderID= senderID, chatID= chatID , date=datetime.utcnow())
    db.session.add(newmessage)
    db.session.commit()
    return newmessage


"""GET FUNCTIONS """
"""--------------------------------------- """
def get_messages_byID(messageID ):
    return Message.query.get(messageID)


def get_messages_by_senderID(senderID):
    return Message.query.get(senderID)


def get_messages_by_chatID(chatID):
    return Message.query.get(chatID)


def get_all_messages():
    return Message.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_message(messageID, text, senderID, chatID, date=datetime.utcnow()):
    updatedmessage = get_message_byID(messageID)
    if updatedmessage:
        updatedmessage.text = text
        updatedmessage.senderID = senderID
        updatedmessage.chatID = chatID
        updatedmessage.date=datetime.utcnow()
        return db.session.commit( updatedmessage)
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_messages(messageID):
    delmessages= get_messages_byID(messageID)
    if delmessages:
        db.session.delete(delmessages)
        return db.session.commit()
    return None


"""--------------------------------------- """