from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_cetluserqueue(CETLUserQ, CETLUserID):
    newcetluserqueue= CETLUserQueue(CETLUserQ=CETLUserQ, CETLUserID=CETLUserID)
    db.session.add(newcetluserqueue)
    db.session.commit()
    return newcetluserqueue

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_celtuserqueue_by_CETLUserID(CETLUserID):
    return CETLUserQueue.query.get(CETLUserID)


def get_celtuserqueue_by_CETLUserQ(CETLUserQ):
    return CETLUserQueue.query.get(CETLUserQ)


def get_all_celtuserqueue():
    return CETLUserQueue.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_celtuserqueue(CETLUserQ, CETLUserID):
    updatedceltuserqueue = get_celtuserqueue_by_CETLUserID(CETLUserID)

    if updatedceltuserqueue:
        updatedceltuserqueue.CETLUserQ = CETLUserQ
        db.session.add(updatedceltuserqueue)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_celtuserqueue(CETLUserID):
    delcetlqueue = get_cetluserqueue_by_ID(CETLUserID)
    if delcetlqueue:
        db.session.delete(delcetlqueue)
        return db.session.commit()
    return None


"""--------------------------------------- """