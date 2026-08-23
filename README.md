
# Customer Churn Prediction AI

### 🔮 Predict. Prevent. Retain.

An **AI-powered Customer Churn Prediction System** that analyzes customer information, services, contract details, and billing behavior to predict whether a customer is likely to **stay or leave**.

The project combines **Machine Learning, Data Preprocessing, Model Comparison, Flask, HTML, CSS, and JavaScript** to create an interactive end-to-end churn prediction application.

---

## 🌟 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses.

Instead of waiting for customers to leave, this project uses machine learning to identify **high-risk customers before they churn**.

The system:

> 📊 Collects customer information
> ⚙️ Preprocesses the data
> 🤖 Trains multiple ML models
> 🏆 Selects the best-performing model
> 🔮 Predicts churn probability
> 💡 Provides AI-based retention recommendations

---

## ✨ Key Features

* 🤖 **AI-powered churn prediction**
* 📈 **Churn probability percentage**
* 🎯 **High / Low churn risk classification**
* 🧠 **Model confidence score**
* 💡 **Personalized retention recommendations**
* 🔬 **Multiple ML algorithms comparison**
* ⚙️ Automated data preprocessing
* 🔤 One-Hot Encoding for categorical features
* 📏 Standard Scaling for numerical features
* 🧹 Missing-value handling
* 🌐 Interactive Flask web application
* 🎨 Modern responsive dashboard
* ⚡ Animated prediction interface
* 📱 Mobile-friendly design

---

# 🧠 Machine Learning Pipeline

```text
                 ┌─────────────────────┐
                 │   Customer Dataset  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Data Cleaning     │
                 │ Missing Values      │
                 │ Data Conversion     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Feature Engineering │
                 │ Numeric + Categorical│
                 └──────────┬──────────┘
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
     Numerical Features           Categorical Features
             │                             │
       Median Imputation            Most Frequent
             │                             │
      Standard Scaling              One-Hot Encoding
             │                             │
             └──────────────┬──────────────┘
                            ▼
                  ┌───────────────────┐
                  │ ML Model Training │
                  └─────────┬─────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Logistic          Random            XGBoost
      Regression          Forest
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                  ┌───────────────────┐
                  │ Model Evaluation  │
                  │ Accuracy          │
                  │ Precision         │
                  │ Recall            │
                  │ F1 Score          │
                  │ ROC-AUC           │
                  └─────────┬─────────┘
                            ▼
                  🏆 Best Model Selected
                            │
                            ▼
                    model.pkl
                            │
                            ▼
                  🌐 Flask Web Application
                            │
                            ▼
                    🔮 Prediction Result
```

---

# 🤖 Machine Learning Models

The project compares multiple classification algorithms:

| Model               | Purpose                       |
| ------------------- | ----------------------------- |
| Logistic Regression | Baseline classification model |
| Decision Tree       | Rule-based classification     |
| Random Forest       | Ensemble learning             |
| Gradient Boosting   | Sequential boosting           |
| XGBoost             | Advanced gradient boosting    |

The models are evaluated using:

* ✅ Accuracy
* ✅ Precision
* ✅ Recall
* ✅ F1 Score
* ✅ ROC-AUC

The model with the best **ROC-AUC score** is automatically selected and saved as:

```text
model.pkl
```

---

# 📊 Dataset

This project uses the **Telco Customer Churn dataset**.

The dataset contains information about:

### 👤 Customer Information

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure

### 📡 Services

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies

### 💳 Billing

* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

### 🎯 Target

```text
Churn

Yes → Customer is likely to leave
No  → Customer is likely to stay
```

---

# 🖥️ Web Application

The project provides a modern web interface where users can enter customer information and instantly receive a prediction.

### Input

Users provide:

```text
Customer Information
        +
Services
        +
Billing Information
        +
Charges
```

### Output

The application provides:

```text
🔴 HIGH CHURN RISK
        OR
🟢 LOW CHURN RISK

Churn Probability
Model Confidence
Prediction
AI Recommendation
Retention Suggestions
```

---

# 🎨 Dashboard

The frontend was designed with a modern AI-dashboard style using:

* HTML5
* CSS3
* JavaScript
* Font Awesome
* Responsive layouts
* Gradient UI
* Glassmorphism-style cards
* Animated progress bars
* Interactive form elements

---

# 🛠️ Tech Stack

| Category             | Technology           |
| -------------------- | -------------------- |
| Programming Language | 🐍 Python            |
| Machine Learning     | Scikit-learn         |
| Advanced ML          | XGBoost              |
| Data Processing      | Pandas               |
| Model Saving         | Joblib               |
| Backend              | Flask                |
| Frontend             | HTML5                |
| Styling              | CSS3                 |
| Interactivity        | JavaScript           |
| Icons                | Font Awesome         |
| Dataset              | Telco Customer Churn |

---

# 📁 Project Structure

```text
Churn/
│
├── 📄 app.py
├── 📄 train_model.py
├── 📄 model.pkl
├── 📄 WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── 📄 index.html
├── 📄 result.html
├── 📄 script.js
├── 📄 style.css
│
└── 📄 README.md
```

> 💡 For a production Flask structure, HTML/CSS/JS files can be organized into `templates/` and `static/` folders.

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

```bash
cd Churn
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn xgboost flask joblib
```

---

# 🧪 Train the Model

Run:

```bash
python train_model.py
```

The training pipeline will:

1. Load the dataset
2. Clean the data
3. Convert numerical values
4. Encode the target
5. Split the dataset
6. Preprocess numerical features
7. Encode categorical features
8. Train multiple ML models
9. Evaluate each model
10. Select the best model
11. Save it as `model.pkl`

---

# 🚀 Run the Application

After training:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You can then enter customer information and click:

### 🧠 Predict Customer Churn

---

# 🔮 How Prediction Works

The application receives customer information from the web form.

```text
User Input
    ↓
Flask
    ↓
Pandas DataFrame
    ↓
Trained ML Pipeline
    ↓
Prediction
    ↓
Churn Probability
    ↓
Risk Classification
    ↓
AI Recommendation
```

---

# 💡 Example Prediction

### 🔴 High Risk

```text
Risk Level: HIGH CHURN RISK

Prediction:
Customer is likely to Churn

Churn Probability:
82.45%

Recommendation:
Contact the customer and provide personalized
retention offers, technical support, or loyalty benefits.
```

### 🟢 Low Risk

```text
Risk Level: LOW CHURN RISK

Prediction:
Customer is likely to Stay

Churn Probability:
18.20%

Recommendation:
Maintain customer engagement and reward customer loyalty.
```

---

# 💼 Real-World Business Value

This project can help businesses:

* 🎯 Identify customers at risk
* 💰 Reduce customer acquisition costs
* 📉 Reduce churn rate
* ❤️ Improve customer retention
* 📊 Support data-driven decisions
* 🎁 Create targeted retention campaigns
* 📈 Increase customer lifetime value

---

# 🔥 Future Improvements

This project can be extended into a more advanced **AI Customer Retention Platform**.

### 🚀 Planned Features

* [ ] 📊 Advanced analytics dashboard
* [ ] 📈 Churn trends and charts
* [ ] 👥 Customer segmentation using clustering
* [ ] 🧠 Explainable AI using SHAP
* [ ] 💬 AI chatbot for customer retention
* [ ] 📧 Automated retention emails
* [ ] 🔔 High-risk customer alerts
* [ ] ☁️ Cloud deployment
* [ ] 🔐 User authentication
* [ ] 🗄️ Database integration
* [ ] 📱 Mobile application
* [ ] 🔄 Real-time prediction API
* [ ] 📊 Business intelligence dashboard

---

# 🧠 Advanced Version Idea

The next version could become:

## **ChurnGuard AI 🛡️**

A complete AI-powered customer retention platform.

```text
Customer Data
      ↓
Churn Prediction
      ↓
Risk Scoring
      ↓
Customer Segmentation
      ↓
Explainable AI
      ↓
AI Retention Strategy
      ↓
Automated Customer Engagement
```

Instead of simply answering:

> **"Will this customer churn?"**

the system could answer:

> **"Why will this customer churn, how likely are they to leave, and what should the company do to retain them?"**

---

# 📈 Skills Demonstrated

This project demonstrates practical knowledge of:

```text
Python
│
├── Pandas
├── Data Cleaning
├── Data Preprocessing
├── Feature Engineering
│
Machine Learning
│
├── Classification
├── Logistic Regression
├── Decision Trees
├── Random Forest
├── Gradient Boosting
├── XGBoost
├── Model Evaluation
└── ROC-AUC
│
Deployment
│
├── Flask
├── HTML
├── CSS
└── JavaScript
```

---

# 👨‍💻 Author

### **Vamshi Bandari**

🎯 Aspiring **AI/ML Engineer | Data Scientist**

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Deep Learning
* Real-world AI Applications

---

# ⭐ Support

If you found this project useful:

⭐ **Star this repository**

🍴 **Fork the project**

🐛 **Report issues**

💡 **Suggest improvements**

---

## 🚀 Build. Predict. Prevent. Retain.

> **"Don't wait for customers to leave. Use AI to know who needs you before they do."**

---
