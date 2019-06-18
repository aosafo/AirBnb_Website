import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/listings2.sqlite"
db = SQLAlchemy(app)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/getCityDetails")
def getCityDetails():

    data = [{
        "location": { "coordinates":[40.7, -73.95]},
        "location": { "coordinates":[40.6, -73.85]}
}]

    return jsonify(data)    
    
# @app.route("/project_analysis", methods=['GET', 'POST'])
# def project_analysis():
    
if __name__ == "__main__":
    app.run(debug=True)