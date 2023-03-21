from App.models import User
from App.database import db


def create_lecturer(lecturerID, firstname, lastname,email, password):
     # create new user
    newuser = User(firstname=firstname, lastname=lastname, password=password, email=email, roleID=2)
    db.session.add(newuser)
    db.session.commit()

    # create new lecturer with userId of newly created user as foreign key
    newlecturer = Lecturer(userId=newuser.userId, lecturerID=lecturerID)
    db.session.add(newlecturer)
    db.session.commit()
    return newlecturer


def create_CETLUser(CETLUserID, firstname, lastname,email, password):
     # create new user
    newuser = User(firstname=firstname, lastname=lastname, password=password, email=email, roleID=2)
    db.session.add(newuser)
    db.session.commit()


    # create new cetluser with userId of newly created user as foreign key
    newcetluser = cetluser(userId=newuser.userId, CETLUserID=newcetluser.CETLUserID)
    db.session.add(newcetluser)
    db.session.commit()
    return newcetluser


def create_CETLAdmin(CETLAdminID, firstname, lastname,email, password):
    # create new user
    newuser = User(firstname=firstname, lastname=lastname, password=password, email=email, roleID=2)
    db.session.add(newuser)
    db.session.commit()


    # create new cetladmin with userId of newly created user as foreign key
    newcetladmin = cetladmin(userId=newuser.userId, CETLAdminID= newcetladmin.CETLAdminID)
    db.session.add(newcetladmin)
    db.session.commit()
    return newcetladmin

#user
def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user(userId):
    return User.query.get(UserId)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

#lecturer
def get_lecturer_by_email(email):
    return lecturer.query.filter_by(email=email).first()

def get_lecturer(lecturerID):
    return lecturer.query.get(lecturerID)

def get_all_lecturer():
    return lecturer.query.all()

def get_all_lecturer_json():
    lecturer= lecturer.query.all()
    if not lecturer:
        return []
    lecturer = [lecturer.toJSON() for lecturer in lecturer]
    return lecturer

#cetl_user
def get_cetluser_by_email(email):
    return CETLUser.query.filter_by(CETLUserID=CETLUserID).first()

def get_cetluser(CETLUserID):
    return CETLUser.query.get(CETLUserID)

def get_all_cetluser():
    return CETLUser.query.all()

def get_all_ccetluser_json():
    cetl_user= CETLUser.query.all()
    if not cetl_user:
        return []
    cetl_user = [cetl_user.toJSON() for cetl_user in cetl_user]
    return cetl_user

#cetlAdmin
def get_cetladmin_by_email(email):
    return CETLAdmin.query.filter_by(email=email).first()

def get_cetladmin(CETLAdminID):
    return CETLAdmin.query.get(CETLAdminID)

def get_all_ccetladmin():
    return CETLAdmin.query.all()

def get_all_cetladmin_json():
   cetl_admin= CETLAdmin.query.all()
    if not cetl_admin:
        return []
    cetl_admin = [cetl_admin.toJSON() for cetl_admin in cetl_admin]
    return cetl_admin

def update_user(id, username):
    user = get_user(UserId)
    if user:
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        user.UserId = userId
        user.roleID =  roleID
        db.session.add(user)
        return db.session.commit()
    return None

def delete_user(userId):
    user = get_user(userId)
    if user:
        db.session.delete(user)
        return db.session.commit()
    return None


    