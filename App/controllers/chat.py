from App.models import *
from App.database import db
from datetime import datetime
 
def create_chat(ChatID, messages, users, chatTime=datetime.utcnow()):
    newchat= newchat(ChatID=ChatID, messages= messages, users= users, chatTime=datetime.utcnow())
    db.session.add(newchat)
    db.session.commit()
    return newchat


"""GET FUNCTIONS """
"""--------------------------------------- """
def get_chat_byID(ChatID ):
    return Chat.query.get(ChatID)


def get_chat_by_users(users):
    return Chat.query.get(users)


def get_all_proposals():
    return Chat.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_chat(ChatID, messages, users, chatTime=datetime.utcnow()):
    updatedchat = get_chat_byID(ChatID)
    if  updatedchat:
         updatedchat.messages = messages
         updatedchat.users = users
         updatedchat.chatTime=datetime.utcnow()
         return db.session.commit(updatedchat)
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_chat(ChatID):
    delchat= get_messages_byID(ChatID)
    if delchat:
        db.session.delete(delchat)
        return db.session.commit()
    return None


"""--------------------------------------- """