# ==========================================================
# CUSTOMER CHURN PREDICTION
# FLASK APPLICATION
# ==========================================================

from flask import Flask, render_template, request
import pandas as pd
import joblib
import webbrowser
from threading import Timer

# ---------------------------------------------------------
# Load Trained Model
# ---------------------------------------------------------

model = joblib.load("model.pkl")

# ---------------------------------------------------------
# Flask App
# ---------------------------------------------------------

app = Flask(__name__)

# ---------------------------------------------------------
# Auto Open Browser
# ---------------------------------------------------------

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

# ---------------------------------------------------------
# Home Page
# ---------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    input_data = pd.DataFrame({

        "gender":[request.form["gender"]],
        "SeniorCitizen":[int(request.form["SeniorCitizen"])],
        "Partner":[request.form["Partner"]],
        "Dependents":[request.form["Dependents"]],
        "tenure":[int(request.form["tenure"])],
        "PhoneService":[request.form["PhoneService"]],
        "MultipleLines":[request.form["MultipleLines"]],
        "InternetService":[request.form["InternetService"]],
        "OnlineSecurity":[request.form["OnlineSecurity"]],
        "OnlineBackup":[request.form["OnlineBackup"]],
        "DeviceProtection":[request.form["DeviceProtection"]],
        "TechSupport":[request.form["TechSupport"]],
        "StreamingTV":[request.form["StreamingTV"]],
        "StreamingMovies":[request.form["StreamingMovies"]],
        "Contract":[request.form["Contract"]],
        "PaperlessBilling":[request.form["PaperlessBilling"]],
        "PaymentMethod":[request.form["PaymentMethod"]],
        "MonthlyCharges":[float(request.form["MonthlyCharges"])],
        "TotalCharges":[float(request.form["TotalCharges"])]

    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    probability_percent = round(probability * 100, 2)

    # ---------------------------------------------------------
    # Prediction Information
    # ---------------------------------------------------------

    if prediction == 1:

        result = "Customer is likely to Churn"

        status = "HIGH CHURN RISK"

        status_color = "danger"

        confidence = probability_percent

        recommendation = (
            "Immediately contact the customer, provide personalized "
            "discounts, recommend a long-term contract, and offer "
            "technical support or loyalty benefits."
        )

        risk_icon = "🔴"

    else:

        result = "Customer is likely to Stay"

        status = "LOW CHURN RISK"

        status_color = "success"

        confidence = round(100 - probability_percent, 2)

        recommendation = (
            "Maintain customer engagement, continue providing good "
            "service quality, reward loyalty, and periodically offer "
            "upgrade plans to retain the customer."
        )

        risk_icon = "🟢"

    return render_template(

        "result.html",

        prediction=result,

        probability=probability_percent,

        confidence=confidence,

        recommendation=recommendation,

        risk=status,

        status_color=status_color,

        risk_icon=risk_icon

    )

# ---------------------------------------------------------
# Run Application
# ---------------------------------------------------------

if __name__ == "__main__":

    Timer(1, open_browser).start()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )