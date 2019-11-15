# Flask dependencies
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Routes handlers
from lib.app_controller import auth_verification, login_as_callback, validate_token_callback

# File system
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# App config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, './db/db.users')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB Init
db = SQLAlchemy(app)
# Marshmallow Init
ma = Marshmallow(app)

# Routes:
# Authorize Callback
@app.route('/oauth/authorize', methods=['GET'])
def auth_callback():
    '''Authentication process'''
    success = auth_verification(request)

    if success: 
        # Return the login page
        frontend = open('./public/login.html')
        view = frontend.read()
        return view

    return {}, 400

# Login-As Callback
@app.route('/login', methods=['GET'])
def login_as():
    '''User access / Create token'''
    access = login_as_callback(request)

    return redirect(access), 307

# Token Callback
@app.route('/oauth/token', methods=['POST'])
def token_callback():
    '''Retrieve Token to ST APP'''
    from lib.token_methods import get_token

    # Retrieve token 
    if validate_token_callback(request):
        code = request.form.get('code')
        grant_type = request.form.get('grant_type')

        '''Either 'authorization_code' & 'refresh_token' grant_types will be handled at <get_token> method'''
        token = get_token(code, grant_type)
        return token


    return {}, 403