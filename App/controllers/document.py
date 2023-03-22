from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_document(facultyID, facultyName, courseCode, courseTitle, documentName, documentType, document, dueDate):
    newDocument = Document(facultyID = facultyID, facultyName = facultyName, courseCode = courseCode, 
                courseTitle= courseTitle, documentName = documentName, documentType = documentType,
                 document = document, dueDate = dueDate)
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

def update_document():
    return


"""--------------------------------------- """

"""DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_document():
    return

"""--------------------------------------- """