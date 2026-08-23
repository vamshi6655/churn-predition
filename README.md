<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,21,27&height=220&section=header&text=Telecom%20Churn%20AI&fontSize=52&fontAlignY=38&desc=Intelligent%20Customer%20Retention%20%26%20Attrition%20Forecasting&descAlignY=60&descAlign=50&fontColor=ffffff" alt="Telecom Churn AI Banner" width="100%"/>

  <br/>

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-Web%20Engine-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  </a>
  <a href="https://scikit-learn.org/">
    <img src="https://img.shields.io/badge/Scikit--Learn-Model%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/Pandas-Data%20Mining-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Interface-HTML5%20%2F%20CSS3%20%2F%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="Frontend"/>
  </a>

  <br/><br/>

  <p align="center">
    <b>Transform raw telecom usage patterns into proactive retention strategies.</b><br/>
    An end-to-end Machine Learning pipeline paired with a lightweight web interface for real-time customer attrition risk scoring.
  </p>

  <p align="center">
    <a href="#-key-features">Key Features</a> •
    <a href="#-architecture--flow">Architecture</a> •
    <a href="#-project-blueprint">Blueprint</a> •
    <a href="#-getting-started">Getting Started</a> •
    <a href="#-telecom-metrics-evaluated">Key Metrics</a>
  </p>

  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="Divider" width="100%"/>

</div>

## 💡 Key Features

* **⚡ Real-Time Inference:** Instantaneous risk classification via Flask microservices.
* **🎯 High-Dimensional Analysis:** Ingests tenure, contract structures, payment habits, and service bundles to evaluate customer risk.
* **💾 Zero-Friction Model Persistence:** Pre-trained binary classification model serialized via `pickle` for low-latency deployment.
* **📱 Responsive Client UI:** Dynamic interface with form validation to explore customer parameters on the fly.

---

## 🏗️ Architecture & Flow

```mermaid
flowchart LR
    A[📄 Raw CSV Data] -->|Data Prep & Training| B(🐍 train_model.py)
    B -->|Export Weights| C[(📦 model.pkl)]
    D[🌐 Web UI: index.html] -->|Submit Customer Profile| E(⚡ Flask app.py)
    C -.->|Load Estimator| E
    E -->|Inference & Scoring| F[📊 result.html Output]

    style A fill:#2D3748,stroke:#4A5568,color:#fff
    style B fill:#3182CE,stroke:#2B6CB0,color:#fff
    style C fill:#D69E2E,stroke:#B7791F,color:#fff
    style D fill:#38A169,stroke:#2F855A,color:#fff
    style E fill:#4A5568,stroke:#2D3748,color:#fff
    style F fill:#E53E3E,stroke:#C53030,color:#fff
