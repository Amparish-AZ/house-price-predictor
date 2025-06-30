
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("rf_model.pkl")

st.title("🏡 German House Price Predictor")
st.write("Enter house details below to get the estimated price (€):")

# User inputs
area = st.number_input("Area (in sqft)", 500, 5000, 1200)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 5, 2)
year_built = st.slider("Year Built", 1980, 2024, 2005)
garage = st.selectbox("Garage", ["No", "Yes"])
location = st.selectbox("Location", ["Berlin", "Dresden", "Frankfurt", "Hamburg", "Leipzig", "Munich"])

# Convert inputs to match model format
garage_binary = 1 if garage == "Yes" else 0
location_map = {"Berlin": 0, "Dresden": 1, "Frankfurt": 2, "Hamburg": 3, "Leipzig": 4, "Munich": 5}
location_encoded = location_map[location]

# Create input DataFrame
input_df = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "year_built": [year_built],
    "garage": [garage_binary],
    "location": [location_encoded]
})

# Predict and show result
if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"🏠 Predicted House Price: €{round(prediction, 2):,}")
