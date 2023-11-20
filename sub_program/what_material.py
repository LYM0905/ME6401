import json
import numpy as np
import pandas as pd
import pyrebase
import requests
import time
from datetime import datetime, timedelta
from flask import Flask, jsonify, request, redirect, url_for, render_template
from sklearn.externals import joblib

# Flask object creation
app = Flask(__name__)

# Pyrebase object creation
config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "databaseURL": "YOUR_DATABASE_URL",
    "storageBucket": "YOUR_STORAGE_BUCKET"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Index page
@app.route("/")
def index():
    return_value = {"message": "Welcome to the Pehchaan API!"}
    json_string = json.dumps(return_value)
    return json_string

@app.route('/view')
def view():
    return render_template('prediction.html')

# Prediction page
@app.route('/predict', methods=['GET'])
def predict():
    clf = joblib.load('model.pkl')
     
    myvar = request.args["myvar"]
    parameter_list = myvar.split(',')

    list_filtered_values = [float(i) for i in parameter_list]
    
    inputarray = [[np.amin(list_filtered_values), np.amax(list_filtered_values), np.ptp(list_filtered_values),
                   np.percentile(list_filtered_values, 75), np.percentile(list_filtered_values, 25),
                   np.median(list_filtered_values), np.mean(list_filtered_values)]]

    prediction = clf.predict(inputarray)
    percentage_predictions = clf.predict_proba(inputarray)

    # Find the highest probability and corresponding material
    materials = ['ceramics', 'plastic', 'wood']  # Adjust this list based on your model's classes
    max_index = np.argmax(percentage_predictions)
    what_material = materials[max_index]

    # Store the result in Firebase (optional)
    db.child("predicted_material").set({"material": what_material})

    return jsonify({'predicted_material': what_material})

# Error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
