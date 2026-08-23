import json
import requests

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "customer-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda value: json.loads(
        value.decode("utf-8")
    ),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ml-inference"
)


API_URL = "http://localhost:8000/predict"


print("Waiting for customer events...")


for message in consumer:

    customer = message.value

    print("RECEIVED FROM KAFKA:")
    print(customer)

    response = requests.post(
        API_URL,
        params=customer
    )

    result = response.json()

    print("MODEL RESULT:")
    print(result)
    print("-" * 50)
