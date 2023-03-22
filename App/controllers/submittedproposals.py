from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_submittedproposals(lecturerID, documentID, dateSubmitted, responseStatus, assignedCetl):
    newproposal= submittedProposals(lecturerID= lecturerID, documentID=documentID, dateSubmitted=dateSubmitted, responseStatus= responseStatus, assignedCetl=assignedCetl)
    db.session.add(newproposal)
    db.session.commit()

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_submittedproposal_byID(submittedID):
    return submittedProposals.query.get(submittedID)


def get_submittedproposal_by_lecturerID(lecturerID):
    return submittedProposals.query.get(lecturerID)


def get_submittedproposal_by_CETLuser(CETLUserID):
    return submittedProposals.query.get(CETLUserID)

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_submittedproposal(submittedID, lecturerID, documentID, dateSubmitted, responseStatus, assignedCetl, CETLUserID):
    updatedproposal = get_submittedproposal_byID(submittedID)
    if updatedproposal:
        updatedproposal.lecturerID = lecturerID
        updatedproposal.documentID = documentID
        updatedproposal.dateSubmitted = dateSubmitted
        updatedproposal.responseStatus = responseStatus
        updatedproposal.assignedCetl = assignedCetl
        updatedproposal.CETLUserID= CETLUserID
        db.session.add(updatedproposal)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_submittedproposal(submittedID):
    delproposal = get_submittedproposal_byID(submittedID)
    if delproposal:
        db.session.delete(delproposal)
        return db.session.commit()
    return None


"""--------------------------------------- """