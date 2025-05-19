from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import asyncio

import json
KAFKA_SEND_MESSAGE_TOPIK = "send_message"
KAFKA_SERVER = "kafka:9092"

KAFKA_RECEIVED_MESSAGE_TOPIC = "received_message"


print("MS2 Consumer started, receive messages...")
async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_SEND_MESSAGE_TOPIK,
        bootstrap_servers=[KAFKA_SERVER],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )
    producer = AIOKafkaProducer(
        bootstrap_servers=[KAFKA_SERVER],
        value_serializer=lambda m: json.dumps(m).encode('utf-8'),
    )
    retries = 0
    connected = False
    while not connected and retries < 10:
        try:
            await consumer.start()
            await producer.start()
            connected = True
        except Exception:
            await asyncio.sleep(1)
            retries += 1

    while True:
        async for message in consumer:
            print(f"Received: {message.value}")
            await producer.send_and_wait(KAFKA_RECEIVED_MESSAGE_TOPIC, message.value)

asyncio.run(consume())
