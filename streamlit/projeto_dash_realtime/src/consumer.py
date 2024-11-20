import json
import os

from confluent_kafka import Consumer
from dotenv import load_dotenv

load_dotenv()

consumer_conf = {
    "bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS"),
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": os.getenv("SASL_USERNAME"),
    "sasl.password": os.getenv("SASL_PASSWORD"),
    "group.id": "streamlit-app",
    "auto.offset.reset": "earliest",
    "session.timeout.ms": 45000,
}

consumer = Consumer(consumer_conf)

consumer.subscribe(["orders"])


def get_message():
    while True:
        message = consumer.poll(1.0)
        if message is None:
            continue
        if message.error():
            print(f"Consumer error: {message.error()}")
            continue

        print(f"Order: {message.value()}")
        return json.loads(message.value().decode("utf-8"))


if __name__ == "__main__":
    while True:
        get_message()
