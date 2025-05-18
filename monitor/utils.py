import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
model = joblib.load(MODEL_PATH)

def predict_failure(temp, vib):
    return model.predict([[temp, vib]])[0]
