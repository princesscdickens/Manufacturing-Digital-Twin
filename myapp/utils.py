import joblib
import os
import pandas as pd

def load_data():
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "data", "machine_data.csv")
    return pd.read_csv(data_path)


MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
model = joblib.load(MODEL_PATH)

def predict_failure(temp, vib):
    return model.predict([[temp, vib]])[0]
