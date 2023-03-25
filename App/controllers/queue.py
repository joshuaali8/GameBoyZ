from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_queue(queueID, documentID, position, dateSubmitted, estimatedResponseTime, assignedCetl):
    newqueue= Queue (queueID=queueID, documentID=documentID, position=position, dateSubmitted=dateSubmitted, estimatedResponseTime=estimatedResponseTime, assignedCetl=assignedCetl)
    db.session.add(newqueue)
    db.session.commit()
    return newqueue

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_queue_byID(queueID):
    return Queue.query.get(queueID)


def get_queue_by_documentID(documentID):
    return Queue.query.get(documentID)


def get_queue_by_dateSubmitted(dateSubmitted):
    return Queue.query.get(dateSubmitted)

def get_queue_by_position(position):
    return Queue.query.get(position)

def get_queue_by_assignedCetl(assignedCetl):
    return Queue.query.get(assignedCetl)



def get_all_queue():
    return Queue.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_queue(queueID, documentID, position, dateSubmitted, estimatedResponseTime, assignedCetl):
    updatedqueue = get_queue_byID(queueID)
    if updatedqueue:
        updatedqueue.documentID = documentID
        updatedqueue.position = position
        updatedqueue.dateSubmitted = dateSubmitted
        updatedqueue.programmeLevel = programmeLevel
        updatedqueue.estimatedResponseTime = estimatedResponseTime
        updatedqueue.assignedCetl = assignedCetl
        db.session.add(updatedqueue)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_queue(queueID):
    delqueue = get_queue_byID(queueID)
    if delqueue:
        db.session.delete(delqueue)
        return db.session.commit()
    return None


"""--------------------------------------- """