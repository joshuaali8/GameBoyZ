from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    __abstract__ = True

    userId = db.Column(db.Integer, primary_key=True)
    roleID =  db.Column(db.Integer, nullable = False)
    email =  db.Column(db.String(120))
    password = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))

    
    def __init__(self, firstname, lastname, password, roleID):
        self.firstname = firstname
        self.lastname = lastname
        self.set_password(password)
        self.roleID = roleID

    def toJSON(self):
        return{
            'userId': self.userId,
            'role_id': self.roleID,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    @staticmethod
    def is_valid_id(id):
        # Check if ID is 9-digit integer
        return isinstance(id, int) and len(str(id)) == 9

    @staticmethod
    def is_email_unique(email):
        # Check if email already exists in database
        return not User.query.filter_by(email=email).first()