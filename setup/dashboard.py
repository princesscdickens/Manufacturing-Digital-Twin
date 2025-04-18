import streamlit as st
import pandas as pd
import joblib
import random

model = joblib.load("model.joblib")

st.title("Digital Twin - Machine Health Monitor")

def simulate_new_reading():
    temperature = round(random.gauss(75, 10), 2)
    vibration = round(random.gauss(0.5, 0.1), 2)
    return temperature, vibration

if st.button("Get New Sensor Reading"):
    temp, vib = simulate_new_reading()
    st.write(f"Temperature: {temp} °F")
    st.write(f"Vibration: {vib} g")
    prediction = model.predict([[temp, vib]])[0]
    st.success("Healthy" if prediction == 0 else "Failure Predicted!")

