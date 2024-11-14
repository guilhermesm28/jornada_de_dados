import pandas as pd
from faker import Faker

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


def generate_fake_orders(start_date="today", end_date="today"):
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


def generate_fake_orders_parquet(n_rows=1000):
    data = [
        generate_fake_orders(start_date="-30d", end_date="-1d") for _ in range(n_rows)
    ]

    pd.DataFrame(data).to_parquet("data/orders.parquet")


if __name__ == "__main__":
    # for _ in range(10):
    #     print(generate_fake_orders())

    generate_fake_orders_parquet()
