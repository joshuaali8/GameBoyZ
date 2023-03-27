from App.models import *
from App.database import db

"""CREATE FUNCTIONS """
"""--------------------------------------- """

def create_date(DateID, Day, Month, Year, Time):
    newdate= Date(DateID= DateID, Day= Day , Month= Month, Year= Year, Time= Time)
    db.session.add(newdate)
    db.session.commit()
    return newdate
"""--------------------------------------- """

"""GET FUNCTIONS """
"""--------------------------------------- """
def get_date_by_dateID( DateID):
    return  Date.query.get( DateID)


def get_date_by_Day(Day):
    return  Date.query.get(Day)


def get_date_by_Month(Month):
    return  Date.query.get(Month)

def get_date_by_Year(Year):
    return  Date.query.get(Year)


def get_all_date():
    return  Date.query.all()

"""--------------------------------------"""

""" UPDATE FUNCTIONS """
"""--------------------------------------- """

def update_date(DateID, Day, Month, Year, Time):
    updateddates = get_date_byID(DateID)
    if updateddates:
        updateddates.Day = Day
        updateddates.Month = Month
        updateddates.Year= Year
        updateddates.Time= Time
        db.session.add(updateddates)
        return db.session.commit()
    return None


"""--------------------------------------- """

""" DELETE FUNCTIONS """
"""--------------------------------------- """

def delete_date(DateID):
    deldates = get_date_byID(DateID)
    if deldates:
        db.session.delete(deldates)
        return db.session.commit()
    return None


"""--------------------------------------- """