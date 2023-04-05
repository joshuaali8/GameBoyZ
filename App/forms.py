from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import InputRequired, EqualTo, Email
from flask_wtf.file import FileField

class SignUp(FlaskForm):
    role = SelectField('Select Role', choices=[(3, 'Lecturer'), (2, 'CETL User'), (1, 'CETL Admin')], validators=[InputRequired()])
    ID = IntegerField('Enter ID', validators=[InputRequired()])
    firstname = StringField('Enter First Name', validators=[InputRequired()])
    lastname = StringField('Enter Last Name', validators=[InputRequired()])
    email = StringField('Enter Email', validators=[Email(), InputRequired()])
    password = PasswordField('Enter New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class ProposeDocument(FlaskForm):
    documentName = StringField('Enter Document Name', validators=[InputRequired()])
    facultyName = StringField('Enter Faculty Name', validators=[InputRequired()])
    courseCode = StringField('Enter Course Code', validators=[InputRequired()])
    courseTitle = StringField('Enter Course Title', validators=[InputRequired()])
    email = StringField('Enter Email', validators=[Email(), InputRequired()])
    document = FileField('Submit File')
    submit = SubmitField('Submit Proposal', render_kw={'class': 'btn waves-effect waves-light white-text'})

