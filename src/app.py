# Created by Immanuel Amirtharaj
# app.py


from flask import Flask, request, render_template
from flask import send_from_directory
from flask import redirect

import os

def create_app():
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	UPLOAD_FOLDER = os.path.join(APP_ROOT, 'images')


	app = Flask(__name__)	# ceate an instance of Flask
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	return app


app = create_app()
import models
import api



@app.route('/') # the route decorator binds a function to a url
def home_page():
	print("home page")
	

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)




