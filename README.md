# 🔧 ML Predictive Maintenance Dashboard

An interactive Machine Learning dashboard that predicts machine failures using industrial sensor data.
Built with Python, Scikit-learn, and Streamlit.

---

## 📌 Project Description

This project implements a Predictive Maintenance system that analyzes machine operating data (temperature, speed, torque, tool wear, etc.) and predicts whether a machine will fail or operate normally.

The model is trained using a Random Forest Classifier and deployed in a Streamlit web dashboard for easy interaction and visualization.

---

## 🎯 Key Features

*  Machine Failure Prediction (ML Model)
*  Upload CSV Dataset
*  Interactive Data Visualization
*  Failure Distribution Charts
*  Trained Random Forest Model

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Matplotlib
* Jupyter Notebook

---

## 🧠 Machine Learning Model

* Model: Random Forest Classifier
* Task: Classification (Failure / No Failure)
* Target Column: `Target`
* Dataset Type: Industrial Predictive Maintenance Data

---

## 📁 Project Structure

```
ML-Predictive-Maintenance/
│
├── app.py                 # Streamlit dashboard application
├── model.pkl              # Trained machine learning model
├── dataset.csv            # Predictive maintenance dataset
├── ML (Random F).ipynb    # Model training notebook
└── README.md              # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib streamlit
```

### 2️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

### 3️⃣ Open in Browser

```
http://localhost:8501
```

Then upload the CSV dataset to get failure predictions and visual analytics.

---

## 📊 Dataset Features

The dataset includes:

* Air temperature [K]
* Process temperature [K]
* Rotational speed [rpm]
* Torque [Nm]
* Tool wear [min]
* Machine Type (L, M, H)
* Target (0 = No Failure, 1 = Failure)

---

##  Future Improvements

* Real-time IoT sensor integration (ESP32 / Arduino)
* Deep Learning model (LSTM)
* Failure probability prediction (%)
* Cloud deployment (Streamlit Cloud)
* Advanced analytics dashboard

---

## 👨‍💻 Author

Ayyoub Hasnaoui
Machine Learning & Automation Engineering Project

---

## ⭐ If you like this project

Give it a star on GitHub to support the work!
