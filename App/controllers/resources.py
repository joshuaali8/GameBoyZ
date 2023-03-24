from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_resources(resourceID, resourceTag, resourceData, resourceName):
    newresources= newresources(resourceID= resourceID, resourceTag= resourceTag, resourceData= resourceData, resourceName= resourceName)
    db.session.add(newresources)
    db.session.commit()
    return newresources

"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_resources_byID(resourceID):
    return Resource.query.get(resourceID)


def get_resources_by_resourceTag(resourceTag):
    return Resource.query.get(resourceTag)


def get_resources_by_resourceName(resourceName):
    return Resource.query.get(resourceName)


def get_all_proposals():
    return Resource.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_resources(resourceID, resourceTag, resourceData, resourceName):
    updatedresources = get_resources_byID(resourceID)
    if updatedresources:
        updatedresources.resourceID= resourceID
        updatedresources.resourceTag = resourceTag
        updatedresources.resourceData = resourceData
        updatedresources.resourceName = resourceName
        db.session.add(updatedresources)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_resources(resourceID):
    delresources = get_resources_byID(resourceID)
    if delresources:
        db.session.delete(delresources)
        return db.session.commit()
    return None


"""--------------------------------------- """