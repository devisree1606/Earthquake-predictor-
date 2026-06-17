from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
with open("earthquake_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    magnitude = float(request.form["magnitude"])
    depth = float(request.form["depth"])
    latitude = float(request.form["latitude"])
    longitude = float(request.form["longitude"])

    sample = [[magnitude, depth, latitude, longitude]]

    prediction = model.predict(sample)

    if prediction[0] == 0:
        result = "Low Earthquake"
    elif prediction[0] == 1:
        result = "Moderate Earthquake"
    else:
        result = "Severe Earthquake"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
