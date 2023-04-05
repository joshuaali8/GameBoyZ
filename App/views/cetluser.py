from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt import jwt_required, current_identity

from.index import index_views

from App.controllers import*

cetluser_views = Blueprint('cetluser_views', __name__, template_folder='../templates')

@cetluser_views.route('/home' , methods = ['GET'])
def get_cetlusermenu_page():
    return render_template('lecturermenu.html')