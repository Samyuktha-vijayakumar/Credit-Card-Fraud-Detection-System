from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def get_live_data(batch_size=20):

    data = []

    for message in consumer:
        data.append(message.value)

        if len(data) >= batch_size:
            break

    return data