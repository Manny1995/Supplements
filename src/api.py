# Created by Immanuel Amirtharaj
# api.py

from flask import Flask, request, render_template
from flask import send_from_directory
from flask import redirect

from app import app


import models
from models import User

import os
import binascii

import json




def contains_user(uname, email):
	res = User.get(username=uname, email=email)
	return res



def create_user(uname, fname, lname, email, password):
	models.open_connection()
	tok = binascii.b2a_hex(os.urandom(20))
	User.create(username=uname, first_name=fname, last_name=lname, email=email, password=password, auth_token=tok)
	models.close_connection()
	return tok


def validate_user_token(token):
	models.open_connection()

	success = True
	token = None

	try:
		tmp = User.get(auth_token=token)
		token = tmp.auth_token
	except User.DoesNotExist:
		success = False

	models.close_connection()

	return {'success' : success, 'token' : token}



def validate_user(uname, password):

	models.open_connection()

	success = True
	token = None

	try:
		tmp = User.get(username=uname, password=password)
		token = tmp.auth_token
	except User.DoesNotExist:
		success = False

	models.close_connection()

	return {'success' : success, 'token' : token}


@app.route('/api/supplements/<supplement_id>', methods=['GET', 'POST'])
def get_supplement_with_id():
	# get supplement with supplement id
	pass



@app.route('/api/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']

	res = validate_user(username, password)
	return json.dumps(res)



@app.route('/api/signup', methods=['POST'])
def signup():
	print("Entering sign up")

	uname = request.form['username']
	fname = request.form['firstname']
	lname = request.form['lastname']
	email = request.form['email']
	password = request.form['password']

	tok = create_user(uname, fname, lname, email, password)
	return tok



# Entry endpoints

@app.route('/api/entry/', methods=['GET', 'POST'])
def list_entries():
	# code to get all entries
	if request.method == 'GET':
		# get list of stuff by offset
		pass
		
	else:
		# insert new entry
		pass
		
@app.route('/api/entry/offset/<entry_offset>')
def entries_with_offset():
	pass
	

@app.route('/api/entry/<entry_id>')
def get_single_entry():
	# get single entries
	print(request.entry_id);
