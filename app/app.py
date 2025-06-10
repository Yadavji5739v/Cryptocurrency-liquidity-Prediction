import pickle
import streamlit as st
import numpy as np
import os


from xgboost import XGBRegressor

model = XGBRegressor()
import os
model_path = os.path.join(os.path.dirname(__file__), "xgb_model.json")
model.load_model(model_path)







import json
from sklearn.preprocessing import MinMaxScaler
import numpy as np

with open('scaler_params.json', 'r') as f:
    scaler_params = json.load(f)

scaler = MinMaxScaler(feature_range=tuple(scaler_params['feature_range']))
scaler.scale_ = np.array(scaler_params['scale_'])
scaler.min_ = np.array(scaler_params['min_'])
scaler.data_min_ = np.array(scaler_params['data_min_'])
scaler.data_max_ = np.array(scaler_params['data_max_'])
scaler.data_range_ = np.array(scaler_params['data_range_'])

# Now scaler is ready to use






# Streamlit UI
st.title("🔮 Cryptocurrency Liquidity Predictor")

market_cap = st.number_input("Market Cap", value=100000000)
total_volume = st.number_input("Total Volume", value=5000000)
rolling_volume = st.number_input("7-Day Rolling Volume", value=4800000)
volatility = st.number_input("7-Day Price Volatility", value=0.02)

if st.button("Predict Liquidity Ratio"):
    features = np.array([[market_cap, total_volume, rolling_volume, volatility]])
    features = scaler.transform(features)
    prediction = model.predict(features)
    st.success(f"💧 Predicted Liquidity Ratio: {prediction[0]:.6f}")
