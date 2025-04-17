# simulate_data.py
import random
import pandas as pd

def generate_data(n=1000):
    data = []
    for _ in range(n):
        temperature = random.gauss(75, 10)  # average 75F, std 10
        vibration = random.gauss(0.5, 0.1)  # average 0.5, std 0.1
        failure = 1 if temperature > 90 or vibration > 0.7 else 0
        data.append([temperature, vibration, failure])
    
    return pd.DataFrame(data, columns=["temperature", "vibration", "failure"])

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("machine_data.csv", index=False)

