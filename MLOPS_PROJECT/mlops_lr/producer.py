"""import requests
import random
import time
import csv
from datetime import datetime


API_URL = "http://localhost:8000/predict"

LOG_FILE = "predictions.csv"


def generate_customer():

    return {
        "age": random.randint(18, 70),
        "monthly_spend": round(random.uniform(20, 150), 2),
        "number_of_logins": random.randint(1, 30),
        "days_since_last_login": random.randint(0, 30),
    }


# Create CSV if it doesn't exist
try:
    with open(LOG_FILE, "x", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "age",
            "monthly_spend",
            "number_of_logins",
            "days_since_last_login",
            "prediction",
            "probability",
            "latency_ms"
        ])

except FileExistsError:
    pass


while True:

    customer = generate_customer()

    #response = requests.post(
    #    API_URL,
    #    params=customer
    #)

    producer.send(
    "customer-events",
    customer
    )



    result = response.json()

    timestamp = datetime.now().isoformat()

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            customer["age"],
            customer["monthly_spend"],
            customer["number_of_logins"],
            customer["days_since_last_login"],
            result["prediction"],
            result["probability"],
            result["latency_ms"]
        ])

    print("=" * 50)

    print("NEW CUSTOMER")

    print(f"Age: {customer['age']}")
    print(f"Monthly spend: ${customer['monthly_spend']}")
    print(f"Logins: {customer['number_of_logins']}")
    print(
        f"Days since last login: "
        f"{customer['days_since_last_login']}"
    )

    print()

    print(f"Prediction: {result['prediction']}")
    print(f"Probability: {result['probability']:.3f}")
    print(f"Latency: {result['latency_ms']:.3f} ms")

    time.sleep(2)

    """


import json
import random
import time

from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


def generate_customer():
    return {
        "age": random.randint(18, 70),
        "monthly_spend": round(random.uniform(20, 150), 2),
        "number_of_logins": random.randint(1, 30),
        "days_since_last_login": random.randint(0, 30),
    }


while True:

    customer = generate_customer()

    producer.send(
        "customer-events",
        value=customer
    )

    producer.flush()

    print("SENT TO KAFKA:")
    print(customer)
    print()

    time.sleep(2)
