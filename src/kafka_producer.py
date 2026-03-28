from kafka import KafkaProducer
import json
import time
import pandas as pd

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

data = pd.read_csv("data/creditcard.csv")

# OPTIONAL: reduce dataset for demo
data = data.sample(500)

for i, row in data.iterrows():

    transaction = row.drop("Class").to_dict()

    producer.send("transactions", value=transaction)

    # send faster (real-time simulation)
    if i % 10 == 0:
        producer.flush()

    print(f"Sent transaction {i}")

    time.sleep(0.1)   # faster streaming

producer.flush()
print("All transactions sent")

