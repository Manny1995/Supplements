# Created by Immanuel Amirtharaj
# api.py

import app
from flask import Flask, request, render_template
from flask import send_from_directory
from flask import redirect
import models

import os





@app.route('/api/supplements/<supplement_id>', methods=['GET', 'POST'])
def get_supplement_with_id():
	# get supplement with supplement id
	pass



@app.route('/api/login', methods=['GET', 'POST'])
def login():

	if request.method == 'GET':
		return render_template('login.html')

	else:
		username = request.form['username']
		password = request.form['password']
		return redirect('/', code=302)




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
