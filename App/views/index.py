from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_manager, login_required
from flask import Flask, flash
from App.controllers import *

from App.forms import*

import json
index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/signup', methods = ['GET'])
def signup_page():
    form = SignUp()
    return render_template('registration.html', form=form)

@index_views.route('/viewResources', methods= ['GET'])
def resource_library():
    return render_template('ResourceLibrary.html')