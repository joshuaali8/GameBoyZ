from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt import jwt_required, current_identity

from.index import index_views

from App.controllers import*

lecturer_views = Blueprint('lecturer_views', __name__, template_folder='../templates')

@lecturer_views.route('/home' , methods = ['GET'])
def get_lecturermenu_page():
    return render_template('lecturermenu.html')

@lecturer_views.route('/submit', methods = ['GET'])
def get_submission_page():
    return render_template('formSubmission.html')
