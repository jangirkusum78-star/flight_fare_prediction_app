# ✈️ Flight Fare Prediction

## 📌 Project Overview

This project aims to predict airline ticket prices using Machine Learning techniques. The objective is to help travelers estimate flight fares based on various factors such as airline, source, destination, journey date, duration, and number of stops.

The project follows a complete machine learning workflow including data preprocessing, exploratory data analysis, feature engineering, model building, hyperparameter tuning, evaluation, and deployment using Streamlit.

---

## 🎯 Problem Statement

Flight ticket prices vary significantly based on multiple factors. Accurate fare prediction can help customers make informed travel decisions and assist businesses in pricing analysis.

The goal of this project is to build a regression model capable of predicting flight prices with high accuracy.

---

## 📂 Dataset Features

The dataset contains flight-related information such as:

* Airline
* Date of Journey
* Source
* Destination
* Route
* Departure Time
* Arrival Time
* Duration
* Total Stops
* Additional Information
* Price (Target Variable)

---

## 🔍 Exploratory Data Analysis (EDA)

Performed detailed exploratory analysis to understand:

* Distribution of flight prices
* Airline-wise fare comparison
* Source and destination trends
* Impact of total stops on fare
* Duration vs Price relationship
* Correlation among numerical features
* Outlier detection and analysis

### Key Insights

* Flights with fewer stops generally have higher prices.
* Airline choice significantly affects ticket cost.
* Duration and total stops strongly influence fare.
* Flight prices vary across different routes and seasons.

---

## 🛠️ Data Preprocessing

### Missing Value Treatment

* Checked for null values.
* Handled missing records appropriately.

### Feature Engineering

Extracted useful features from date and time columns:

* Journey Day
* Journey Month
* Departure Hour
* Departure Minute
* Arrival Hour
* Arrival Minute
* Duration in Minutes

### Categorical Encoding

Encoded categorical variables such as:

* Airline
* Source
* Destination
* Route
* Additional Information

### Feature Scaling

Applied StandardScaler for linear models to normalize feature values.

---

## 🤖 Machine Learning Models

The following regression models were trained and evaluated:

### 1. Linear Regression

Used as a baseline model.

**Results**

* MAE ≈ 1984
* MSE ≈ 7.8 Million
* R² ≈ 0.63

### 2. Ridge Regression (L2 Regularization)

Applied regularization to reduce coefficient variance.

**Results**

* Performance similar to Linear Regression
* No significant improvement observed

### 3. Random Forest Regressor

Used ensemble learning to capture nonlinear relationships.

**Results**

* MAE ≈ 1248
* MSE ≈ 4.2 Million
* R² ≈ 0.80

### 4. XGBoost Regressor (Final Model)

Applied hyperparameter tuning to improve performance.

**Advantages**

* Captures complex nonlinear patterns
* Better generalization capability
* Lower prediction error

**Final Selection**
XGBoost was selected as the final model due to its superior predictive performance.

---

## ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed using RandomizedSearchCV to optimize model performance.

Parameters tuned included:

* n_estimators
* max_depth
* learning_rate
* subsample
* colsample_bytree

---

## 📊 Evaluation Metrics

Models were evaluated using:

### Mean Absolute Error (MAE)

Measures average prediction error.

### Mean Squared Error (MSE)

Penalizes larger prediction errors.

### R² Score

Measures the proportion of variance explained by the model.

---

## 📈 Model Comparison

| Model             | MAE                   | MSE          | R² Score   |
| ----------------- | --------------------- | ------------ | ---------- |
| Linear Regression | ~1984                 | ~7.8M        | 0.63       |
| Ridge Regression  | ~1984                 | ~7.8M        | 0.63       |
| Random Forest     | ~1248                 | ~4.2M        | 0.80       |
| XGBoost           | Best Performing Model | Lowest Error | Highest R² |

---

## 🚧 Challenges Faced

* Handling multiple categorical features.
* Feature engineering from date and time columns.
* Deciding whether to retain route-related features.
* Managing notebook complexity during experimentation.
* Hyperparameter tuning increased training time.
* Ensuring preprocessing consistency during deployment.

---

## 🚀 Model Deployment

The trained model was deployed using **Streamlit** to provide a simple and interactive web interface.

### Deployment Workflow

1. Trained final model.
2. Saved model using Joblib.
3. Built Streamlit application.
4. Created prediction interface.
5. Connected application with trained model.
6. Deployed application online.

### Technologies Used

* Python
* Streamlit
* Scikit-Learn
* XGBoost
* Pandas
* NumPy
* Joblib

---

## 🖥️ Application Features

* User-friendly interface
* Real-time fare prediction
* Interactive input fields
* Fast response time
  

---

## 🏗️ Project Structure

```text
Flight_Fare_Prediction/
│
├── Data/
├── Notebook/
│   └── Flight_Fare_Prediction.ipynb
│
├── app.py
├── flight_model.pkl
├── requirements.txt
├── README.md
│
└── Streamlit Deployment Files
```

---

## 🧰 Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost

### Deployment

* Streamlit

### Version Control

* Git
* GitHub

## Deployment
https://jangirkusum78-star-flight-fare-prediction-app-app1-3rg2t2.streamlit.app/

---

## 🎓 Key Learnings

Through this project, I gained hands-on experience in:

* Data preprocessing and cleaning
* Feature engineering
* Exploratory Data Analysis
* Regression modeling
* Ensemble learning methods
* Hyperparameter tuning
* Model evaluation
* Streamlit deployment
* Git and GitHub workflow

---

## 📌 Future Improvements

* Integrate real-time flight data APIs.
* Improve feature engineering using seasonal trends.
* Experiment with LightGBM and CatBoost.
* Deploy using cloud services for scalability.
* Add model monitoring and performance tracking.

---
--- 

**Kusum Jangid**

Aspiring Data Scientist passionate about Machine Learning, Data Analysis, and building end-to-end predictive solutions.
