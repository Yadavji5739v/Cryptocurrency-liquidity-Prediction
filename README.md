# 🪙 Cryptocurrency Liquidity Prediction for Market Stability

## 📌 Project Overview

Cryptocurrency markets are known for their high volatility and unpredictable nature. One of the key indicators of market stability is **liquidity** — the ease with which a cryptocurrency can be bought or sold without impacting its price significantly.

This project aims to build a **machine learning model** that predicts **cryptocurrency liquidity levels** based on historical price, volume, volatility, and engineered financial indicators. The goal is to help traders, investors, and exchanges detect potential liquidity crises early and make informed decisions to reduce risk.

---

## 🔍 Problem Statement

Lack of liquidity in cryptocurrency markets can lead to extreme price fluctuations and pose significant risks to market participants. By predicting liquidity based on market features, this project aims to contribute to **early detection of liquidity shortages** and promote **market stability**.

---

## 🧠 Objectives

- Predict cryptocurrency liquidity using machine learning models.
- Analyze historical market data including price, volume, and volatility.
- Engineer features relevant to liquidity trends such as moving averages and ratios.
- Deploy a user-friendly interface to predict and visualize liquidity levels.

---

## 📂 Dataset

- Source: [CoinGecko](https://www.coingecko.com/)
- Format: CSV
- Features: Market Cap, Price, Trading Volume, etc.
- Duration: Historical data for 2016–2017 and current snapshot (`coin_gecko_2022-03-16.csv`)

---

## 🔧 Tech Stack

- **Python**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn**, **XGBoost**
- **Streamlit** (for web deployment)

---

## 🔨 Project Pipeline

1. **Data Collection**
2. **Data Cleaning & Preprocessing**
3. **Exploratory Data Analysis (EDA)**
4. **Feature Engineering**
5. **Model Training & Evaluation**
6. **Hyperparameter Tuning**
7. **Model Deployment using Streamlit**
8. **Documentation & Reporting**

---

## 📊 Evaluation Metrics

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

---

## 🚀 Deployment

This project includes a simple **Streamlit web app** that allows users to input market data and receive **real-time liquidity predictions**.

To run the app locally:

```bash
streamlit run app.py
