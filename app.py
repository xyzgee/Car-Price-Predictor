import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('models/car_price_model.pkl')

# Streamlit app title
st.title("Car Price Predictor")

# Input fields for the features
name = st.text_input("Car Name")
year = st.number_input("Year", min_value=1900, max_value=2023, value=2020)
km_driven = st.number_input("Kilometers Driven", min_value=0)
fuel = st.selectbox("Fuel Type", options=["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", options=["Individual", "Dealer", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", options=["Manual", "Automatic"])
owner = st.selectbox("Owner", options=["First Owner", "Second Owner", "Third Owner", "Fourth & Above"])

# Button to make prediction
if st.button("Predict Price"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner]
    })

    # Encode the categorical variables (you may need to adjust this based on your encoding method)
    input_data['fuel'] = input_data['fuel'].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4})
    input_data['seller_type'] = input_data['seller_type'].map({'Individual': 0, 'Dealer': 1, 'Trustmark Dealer': 2})
    input_data['transmission'] = input_data['transmission'].map({'Manual': 0, 'Automatic': 1})
    input_data['owner'] = input_data['owner'].map({'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2, 'Fourth & Above': 3})

    # Make prediction
    predicted_price = model.predict(input_data)

    # Display the result
    st.success(f"The predicted price of the car is: ₹{predicted_price[0]:,.2f}")
