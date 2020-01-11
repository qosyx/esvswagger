"""
Main module of the server file
"""
# from core import *
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
# 3rd party moudles
from flask import render_template
import connexion
from flask_cors import CORS
import os

# create the application instance
app = connexion.App(__name__, specification_dir="./")
# Cead the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")
CORS(app.app)

# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")
# @app.route('/upload', methods=['GET', 'POST'])
# def get_image():
        
# 		if 'files[]' not in request.files:
#     			return redirect(request.url)
# 		files = request.files.getlist('files[]')
       
# 		for file in files:
# 			if file:
# 				filename = secure_filename(file.filename)
# 				file.save(os.path.join("files", filename))
                    
# 		flash('File(s) successfully uploaded')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=False, port=int
    (os.environ.get("PORT", 5000)))