<div align="center">

# 📊 Telco Customer Churn Prediction Engine

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-Interactive-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<p align="center">
  <b>A Machine Learning web application designed to predict telecom customer attrition and assist in retention strategies.</b>
</p>

</div>

---

## 📌 Project Overview

Customer churn directly impacts revenue and lifetime customer value in the telecommunications industry. This project utilizes the **Telco Customer Churn dataset** to train a classification model, serialized via pickle, and served through a responsive Flask web application for real-time predictions.

---

## 📁 Repository Structure

```text
Churn-main/
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Raw dataset containing customer demographics & service usage
├── train_model.py                        # Model training, evaluation, and serialization pipeline
├── model.pkl                             # Trained and serialized machine learning model
├── app.py                                # Flask backend handling routes and inference
├── index.html                            # Input form interface for customer parameters
├── result.html                           # Prediction output and probability display
├── script.js                             # Client-side validation and interactivity
└── style.css                             # Custom layout styling and design
⚙️ Tech Stack & ToolsMachine Learning & Data Processing: Python, Scikit-Learn, Pandas, NumPy, Pickle  Backend Application: Flask  Frontend Design: HTML5, CSS3, JavaScript  🚀 Quick Start Guide1. Clone the RepositoryBashgit clone [https://github.com/](https://github.com/)<your-username>/<repo-name>.git
cd Churn-main
2. Set Up a Virtual EnvironmentBash# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install flask scikit-learn pandas numpy
4. Train the Model (Optional)If you want to retrain the classifier on the dataset:Bashpython train_model.py
5. Launch the Web AppBashpython app.py
Open your browser and navigate to:Plaintext[http://127.0.0.1:5000/](http://127.0.0.1:500

