# Created by Immanuel Amirtharaj
# app.py


from flask import Flask, request, render_template
from flask import send_from_directory
from flask import redirect
import models

import os


#import models here
#from models import Post
#import post_db


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'images')


app = Flask(__name__)	# ceate an instance of Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/') # the route decorator binds a function to a url
def home_page():
	print("home page")
	

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)




