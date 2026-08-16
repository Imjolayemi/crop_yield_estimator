import streamlit as st
import pandas as pd
import joblib

# Load model and feature list
model = joblib.load("../models/crop_yield_model.pkl")
feature_names = joblib.load("../models/model_features.pkl")

st.title("🌾 Crop Yield Estimator")
st.write("Enter farm and season details below to estimate expected crop yield.")

state = st.selectbox("State", ["Kano", "Kaduna", "Benue", "Niger", "Oyo", "Rivers", "Other"])
crop_type = st.selectbox("Crop Type", ["Maize", "Cassava", "Rice", "Sorghum", "Yam"])
farm_size_ha = st.number_input("Farm Size (hectares)", min_value=0.1, value=2.0)
avg_rainfall_mm = st.number_input("Average Rainfall (mm)", min_value=0.0, value=150.0)
avg_temperature_c = st.number_input("Average Temperature (°C)", min_value=0.0, max_value=50.0, value=28.0)
soil_ph = st.slider("Soil pH", 3.0, 9.0, 6.5)
soil_type = st.selectbox("Soil Type", ["Clay", "Sandy", "Loamy"])
fertilizer_kg_per_ha = st.number_input("Fertilizer (kg/ha)", min_value=0.0, value=100.0)
pesticide_used = st.selectbox("Pesticide Used?", ["Yes", "No"])
irrigation_used = st.selectbox("Irrigation Used?", ["Yes", "No"])
seed_variety = st.selectbox("Seed Variety", ["Local", "Improved"])

if st.button("Estimate Yield"):
    rainfall_per_ha = avg_rainfall_mm / farm_size_ha
    fertilizer_efficiency_proxy = fertilizer_kg_per_ha / (soil_ph + 1)

    input_df = pd.DataFrame([{
        "state": state,
        "crop_type": crop_type,
        "farm_size_ha": farm_size_ha,
        "avg_rainfall_mm": avg_rainfall_mm,
        "avg_temperature_c": avg_temperature_c,
        "soil_ph": soil_ph,
        "soil_type": soil_type,
        "fertilizer_kg_per_ha": fertilizer_kg_per_ha,
        "pesticide_used": pesticide_used,
        "irrigation_used": irrigation_used,
        "seed_variety": seed_variety,
        "rainfall_per_ha": rainfall_per_ha,
        "fertilizer_efficiency_proxy": fertilizer_efficiency_proxy
    }])

    # Ensure column order matches training
    input_df = input_df[feature_names]

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Yield: **{prediction:.2f} tonnes/hectare**")
    st.caption(f"For a {farm_size_ha:.1f} hectare farm, that's roughly **{prediction * farm_size_ha:.2f} tonnes total**.")