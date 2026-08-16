import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Crop Yield Estimator", page_icon="🌾", layout="centered")

st.title("🌾 AI Crop Yield Estimator")
st.write("Welcome to the AI Farming Assistant! Enter your farm details below, and the AI will predict how many tonnes of crops you will harvest per hectare.")

# 1. Find the exact folder where this app.py file lives
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Build the exact path to the models folder
model_path = os.path.join(current_dir, "..", "models", "crop_yield_model.pkl")
features_path = os.path.join(current_dir, "..", "models", "model_features.pkl")

st.header("📝 Enter Farm Details")

col1, col2 = st.columns(2)

with col1:
    # All 36 States + FCT, in alphabetical order!
    nigerian_states = [
        "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", 
        "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT", 
        "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", 
        "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", 
        "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"
    ]
    state = st.selectbox("State", nigerian_states) 
    
    crop_type = st.selectbox("Crop Type", ["Cassava", "Yam", "Maize", "Sorghum", "Rice"])
    soil_type = st.selectbox("Soil Type", ["Loamy", "Sandy", "Clay"])
    seed_variety = st.selectbox("Seed Variety", ["Local", "Improved"])
    pesticide_used = st.selectbox("Pesticide Used?", ["Yes", "No"])
    irrigation_used = st.selectbox("Irrigation Used?", ["Yes", "No"])

with col2:
    farm_size_ha = st.number_input("Farm Size (Hectares)", min_value=0.1, value=2.0)
    avg_rainfall_mm = st.number_input("Average Rainfall (mm)", min_value=100.0, value=1200.0)
    avg_temperature_c = st.number_input("Average Temperature (°C)", min_value=10.0, value=27.0)
    soil_ph = st.number_input("Soil pH", min_value=1.0, max_value=14.0, value=6.0)
    fertilizer_kg_per_ha = st.number_input("Fertilizer (kg per Hectare)", min_value=0.0, value=100.0)

if st.button("🚀 Predict Crop Yield"):
    
    # The AI expects 14 columns, so we have to calculate our 3 special columns right here.
    optimal_ph = 1 if 5.5 <= soil_ph <= 7.0 else 0
    fertilizer_efficiency_proxy = fertilizer_kg_per_ha / (soil_ph + 1)
    
    water_stress_flag = 0
    if avg_rainfall_mm < 600 and irrigation_used == "No":
        water_stress_flag = 1
        
    # We put everything into a Pandas DataFrame
    input_df = pd.DataFrame({
        'state': [state],
        'crop_type': [crop_type],
        'farm_size_ha': [farm_size_ha],
        'avg_rainfall_mm': [avg_rainfall_mm],
        'avg_temperature_c': [avg_temperature_c],
        'soil_ph': [soil_ph],
        'soil_type': [soil_type],
        'fertilizer_kg_per_ha': [fertilizer_kg_per_ha],
        'pesticide_used': [pesticide_used],
        'irrigation_used': [irrigation_used],
        'seed_variety': [seed_variety],
        'optimal_ph': [optimal_ph],
        'fertilizer_efficiency_proxy': [fertilizer_efficiency_proxy],
        'water_stress_flag': [water_stress_flag]
    })
    
    # Ensure column order matches training exactly!
    input_df = input_df[feature_names]
    
    prediction = model.predict(input_df)
    
    # Display the result to the farmer with celebration balloons!
    st.success(f"🌟 Predicted Yield: **{prediction[0]:.2f} Tonnes per Hectare!**")
    st.caption(f"For a {farm_size_ha:.1f} hectare farm, that's roughly **{prediction[0] * farm_size_ha:.2f} tonnes total**.")
    st.balloons()