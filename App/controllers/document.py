from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_document(documentID, resourceID, queueID, lecturerID, CETLUserID, facultyID, facultyName, programmeName, 
    courseCode, documentName, documentType, document, State, Level, dueDate):
    newDocument = Document( documentID= documentID, resourceID= resourceID,queueID= queueID, lecturerID= lecturerID,CETLUserID= CETLUserID, facultyID= facultyID, 
    facultyName= facultyName, programmeName= programmeName, courseCode= courseCode,documentName= documentName, documentType= documentType, document= document, State= State, Level= Level, dueDate= dueDate)
    db.session.add(newDocument)
    db.session.commit()
    return newDocument

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """

def get_document_by_id(documentID):
    return Document.query.get(documentID)

def get_document_by_name(documentName):
    return Document.query.filter_by(documentName=documentName).first()

def get_all_documents():
    return Document.query.all()


"""--------------------------------------- """

"""UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_documents(documentID, resourceID, queueID, lecturerID, CETLUserID, facultyID, facultyName, programmeName, 
    courseCode, documentName, documentType, document, State, Level, dueDate):
    updateddocuments = get_document_by_ID(documentID)
    if updateddocuments:
        updateddocuments.resourceID = resourceID
        updateddocuments.queueID = queueID
        updateddocuments.lecturerID = lecturerID
        updateddocuments.CETLUserID = CETLUserID
        updateddocuments.facultyID = facultyID
        updateddocuments.facultyName = facultyName
        updateddocuments.programmeName = programmeName
        updateddocuments.courseCode = courseCode
        updateddocuments.documentName = documentType
        updateddocuments.document = document
        updateddocuments.State = State
        updateddocuments.Level = Level
        updateddocuments.dueDate = dueDate
        db.session.add(updateddocuments)
        return db.session.commit()
    return None


"""--------------------------------------- """

"""DELETE FUNCTIONS """
"""--------------------------------------- """
def delete_documents(documentID):
    deldocument = get_document(documentID)
    if deldocument:
        db.session.delete(deldocument)
        return db.session.commit()
    return None

"""--------------------------------------- """