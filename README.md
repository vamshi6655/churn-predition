# 📊 Customer Churn Prediction

A machine learning web app that predicts whether a telecom customer is likely to churn, built with **scikit-learn** and served through a **Flask** dashboard. Enter a customer's profile (contract type, tenure, billing, services used, etc.) and get an instant churn risk score with a retention recommendation.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?style=flat-square&logo=flask)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-006ACC?style=flat-square)

---

## 📌 Overview

Customer churn — when a subscriber cancels their service — is one of the costliest problems for telecom companies. This project trains and compares five classification models on the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn), picks the best performer by ROC-AUC, and exposes it through a simple web dashboard where you can plug in a customer's details and get:

- A **churn prediction** (Stay / Churn)
- A **confidence / probability score**
- A **plain-language retention recommendation**

---

## 🧠 How It Works

```
CSV Dataset  →  Preprocessing (impute, scale, one-hot encode)
             →  Train 5 models (LogReg, Decision Tree, Random Forest,
                 Gradient Boosting, XGBoost)
             →  Pick best model by ROC-AUC
             →  Save as model.pkl
             →  Flask app loads model.pkl and serves predictions
```

**Models compared** (`train_model.py`):
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

Each model is wrapped in a single `sklearn` `Pipeline` (preprocessing + classifier), so `model.pkl` is a ready-to-use, self-contained pipeline — no separate encoders/scalers to manage.

---

## 📁 Project Structure

```
Churn-main/
│
├── app.py                                   ← Flask app (routes + prediction logic)
├── train_model.py                            ← Trains all 5 models, saves the best as model.pkl
├── model.pkl                                  ← Pre-trained best model (sklearn Pipeline)
├── WA_Fn-UseC_-Telco-Customer-Churn.csv       ← Training dataset (7,043 customers)
├── index.html                                 ← Input form (churn prediction dashboard)
├── result.html                                ← Prediction result page
├── style.css                                  ← Dashboard styling
└── script.js                                  ← Frontend interactivity
```

> **Note:** `app.py` expects Jinja templates in a `templates/` folder and static assets in `static/css/` and `static/js/`. Before running the app, move the files accordingly (see [Setup](#-setup--installation) below) or adjust the paths in `app.py` to match a flat layout.

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/vamshibandari/Churn.git
cd Churn
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask pandas scikit-learn xgboost joblib
```

### 4. Arrange files for Flask

Flask looks for HTML in `templates/` and CSS/JS in `static/`:

```bash
mkdir -p templates static/css static/js
mv index.html result.html templates/
mv style.css static/css/
mv script.js static/js/
```

Update the `href`/`src` references in `index.html` and `result.html` if they don't already point to `static/css/style.css` and `static/js/script.js`.

### 5. (Optional) Retrain the model

`model.pkl` is already included, but to retrain from scratch:

```bash
mkdir -p data
mv WA_Fn-UseC_-Telco-Customer-Churn.csv data/
python train_model.py
```

This prints accuracy/precision/recall/F1/ROC-AUC for each model and saves the best one as `model.pkl`.

### 6. Run the app

```bash
python app.py
```

The app auto-opens your browser at **http://127.0.0.1:5000//**.

---

## 🌐 Usage

1. Fill in the customer form — demographics, account info (tenure, contract, billing), and subscribed services.
2. Submit to get:
   - **Prediction:** Likely to Churn / Likely to Stay
   - **Risk level:** HIGH CHURN RISK 🔴 or LOW CHURN RISK 🟢
   - **Confidence %**
   - **Recommended action** (e.g., discounts and outreach for high-risk customers, loyalty rewards for low-risk ones)

---

## 📊 Dataset

**Telco Customer Churn** — 7,043 customers, 21 features including:

| Category | Features |
|---|---|
| Demographics | gender, SeniorCitizen, Partner, Dependents |
| Account | tenure, Contract, PaperlessBilling, PaymentMethod |
| Services | PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies |
| Billing | MonthlyCharges, TotalCharges |
| Target | Churn (Yes/No) |

---

## 🛠️ Tech Stack

- **Python** — core language
- **pandas** — data loading and cleaning
- **scikit-learn** — preprocessing pipeline, model training, evaluation
- **XGBoost** — gradient-boosted tree classifier
- **Flask** — web server and routing
- **joblib** — model serialization
- **HTML/CSS/JS** — dashboard front end

---

## 🔮 Future Improvements

- Add model explainability (SHAP/LIME) to justify individual predictions
- Persist prediction history to a database
- Add batch prediction via CSV upload
- Containerize with Docker for easier deployment
- Add unit tests and CI

---

<div align="center">

**Built by Vamshi Bandari**

</div>
