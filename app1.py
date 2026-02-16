#import streamlit as st
#import joblib
#import numpy as np

#model = joblib.load("flight_model.pkl")
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# -------------------------
# Load model + columns
# -------------------------
model = joblib.load("flight_model.pkl")
columns = joblib.load("columns.pkl")

st.title("✈️ Flight Price Prediction App")

st.write("Enter flight details to estimate ticket price")

# -------------------------
# User Inputs
# -------------------------

airline = st.selectbox("Airline", [
    "IndiGo","Air India","Jet Airways","SpiceJet","Vistara","Go Air"
])

source = st.selectbox("Source", [
    "Delhi","Kolkata","Mumbai","Chennai","Bangalore"
])

destination = st.selectbox("Destination", [
    "Cochin","Delhi","New Delhi","Hyderabad","Kolkata","Banglore"
])

total_stops = st.selectbox("Total Stops", [0,1,2,3])

journey_day = st.slider("Journey Day", 1, 31)
journey_month = st.slider("Journey Month", 1, 12)

dep_slot = st.selectbox("Departure slot", 
["evening","early morning","afternoon","morning"]
)
#streamlit.write("Note: Departure slot is categorized based on typical flight departure times.")
arr_slot = st.selectbox("Arrival slot", 
["early morning","morning","afternoon","evening"]
)

Duration_min = st.number_input("Total Duration (minutes)", min_value=30, max_value=3000)

# -------------------------
# Simple Encoding Maps
# (Replace with YOUR encoding if different)
# -------------------------

airline_map = {
    "IndiGo":0,"Air India":1,"Jet Airways":2,"SpiceJet":3,"Vistara":4,"Go Air":5
}

source_map = {
    "Delhi":0,"Kolkata":1,"Mumbai":2,"Chennai":3,"Bangalore":4
}

dest_map = {
    "Cochin":0,"Delhi":1,"New Delhi":2,"Hyderabad":3,"Kolkata":4,"Banglore":5
}

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Price"):

    input_dict = {
        "Airline": airline_map[airline],
        "Source": source_map[source],
        "Destination": dest_map[destination],
        "Total_Stops": total_stops,
        "Journey_Day": journey_day,
        "Journey_Month": journey_month,
        "dep_slot": dep_slot,
        "arr_slot": arr_slot,
        "Duration": Duration_min
    }

    # convert to dataframe
    input_df = pd.DataFrame([input_dict])

    # align columns with training columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Flight Price: ₹ {round(prediction,2)}")
