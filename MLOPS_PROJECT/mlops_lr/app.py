import time
from fastapi import FastAPI
import joblib
import numpy as np


app = FastAPI()

model = joblib.load("model.pkl")


@app.get("/")
def home():
    return {
        "message": "ML model is alive!"
    }


@app.post("/predict")
def predict(
    age: int,
    monthly_spend: float,
    number_of_logins: int,
    days_since_last_login: int
):

    start_time = time.perf_counter()

    X = np.array([[
        age,
        monthly_spend,
        number_of_logins,
        days_since_last_login
    ]])

    probability = model.predict_proba(X)[0][1]

    prediction = int(probability >= 0.5)

    latency_ms = (time.perf_counter() - start_time) * 1000

    return {
        "prediction": prediction,
        "probability": float(probability),
        "latency_ms": round(latency_ms, 3)
    }
