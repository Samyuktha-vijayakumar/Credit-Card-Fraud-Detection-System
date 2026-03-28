# 💳 Credit Card Fraud Detection System

## 📌 Overview

This project is a **Machine Learning-based Credit Card Fraud Detection System** that identifies fraudulent transactions in real-time.
It uses advanced data preprocessing and classification models to distinguish between legitimate and fraudulent transactions.

---

## 🚀 Features

* 🔍 Detects fraudulent transactions with high accuracy
* ⚡ Real-time prediction using trained ML model
* 📊 Interactive dashboard built with Streamlit
* 📁 Upload CSV file for batch predictions
* 🧠 Uses trained pipeline model for preprocessing + prediction

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * XGBoost
  * Joblib
* **Frontend:** Streamlit
* **Deployment:** Render
* **Model Storage:** Google Drive

---

## 📂 Project Structure

```
credit-card-fraud-detection/
│
├── app/
│   └── streamlit_dashboard.py   # Streamlit UI
│
├── src/
│   ├── preprocess.py            # Data preprocessing
│   ├── train_model.py           # Model training
│   ├── predict.py               # Prediction logic
│   └── utils.py                 # Helper functions
│
├── models/                      # Model (downloaded at runtime)
├── data/                        # Dataset (not included)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Credit-Card-Fraud-Detection-System.git
cd Credit-Card-Fraud-Detection-System
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

 Run the application

```
streamlit run app/streamlit_dashboard.py
```

---

  Live Demo

 https://credit-card-fraud-detection-system-e3ku.onrender.com

---

 Dataset

The dataset is not included in this repository due to size limitations.

You can download it from:

* Kaggle Credit Card Fraud Detection Dataset

---

 Model Details

* Algorithm: XGBoost / ML Pipeline
* Handles imbalanced data
* Preprocessing + model combined using pipeline

---

## 🔄 Workflow

1. Upload transaction data (CSV)
2. Preprocess data
3. Load trained model
4. Predict fraud probability
5. Display results in UI

---

## 📌 Future Improvements

* 🔥 Real-time streaming using Kafka
* 📈 Model performance dashboard
* 🌍 API integration using FastAPI
* 🔐 Enhanced fraud detection with deep learning

---

## 👩‍💻 Author

**Samyuktha Vijayakumar**

* AI & Data Science Student



## ⭐ Acknowledgements

* Kaggle for dataset
* Open-source ML community
