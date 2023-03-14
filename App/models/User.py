from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    roleID =  db.Column(db.Integer)
    email =  db.Column(db.String(120))
    password = db.Column(db.String(120), nullable=False)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))

    
    def __init__(self, firstname, lastname, password):
        self.firstname(firstname)
        self.lastname(lastname)
        self.set_password(password)

    def toJSON(self):
        return{
            'userId': self.userId,
            'firstname': self.firstname,
            'lastname': self.lastname
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

