import json
import os

import pandas as pd
from confluent_kafka import Producer
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

fake = Faker("pt_BR")

regions = ["Sul", "Sudeste", "Nordeste", "Norte", "Centro-Oeste"]

vendors = ["Guilherme", "Giulia", "Scooby"]

products = [
    ("Caneta", 10),
    ("Borracha", 2),
    ("Lapis", 4),
    ("Caderno", 15),
    ("Lapiseira", 7),
]


def generate_fake_order(start_date="today", end_date="today"):
    quantity = fake.random_int(min=1, max=10)
    product = fake.random_element(elements=products)
    product_name = product[0]
    total_price = product[1] * quantity

    return {
        "order_id": fake.uuid4(),
        "order_date": str(fake.date_between(start_date=start_date, end_date=end_date)),
        "region": fake.random_element(elements=regions),
        "vendor": fake.random_element(elements=vendors),
        "product_name": product_name,
        "quantity": quantity,
        "total_price": total_price,
    }


def generate_fake_order_parquet(n_rows=1000):
    data = [
        generate_fake_order(start_date="-30d", end_date="-1d") for _ in range(n_rows)
    ]

    pd.DataFrame(data).to_parquet("data/orders.parquet")


producer_conf = {
    "bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS"),
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": os.getenv("SASL_USERNAME"),
    "sasl.password": os.getenv("SASL_PASSWORD"),
}

producer = Producer(producer_conf)


def generate_message(data):
    key = data["order_id"]
    value = json.dumps(data).encode("utf-8")
    producer.produce(topic="orders", key=key, value=value)
    print(f"Order {key} sent")
    producer.flush()


if __name__ == "__main__":
    # for _ in range(10):
    #     print(generate_fake_order())

    # generate_fake_order_parquet()

    while True:
        data = generate_fake_order()
        generate_message(data)
