import json
from aiokafka import AIOKafkaProducer
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()
KAFKA_SERVER = "kafka:9092"
KAFKA_TOPIK = "send_message"
producer = AIOKafkaProducer(
    bootstrap_servers=[KAFKA_SERVER],
    value_serializer=lambda m: json.dumps(m).encode('utf-8'),
)

class MessageDTO(BaseModel):
    message: str

@app.post('/send-message')
async def send_message(message: MessageDTO):
    print(message.message)
    await producer.start()
    try:
        await producer.send_and_wait(KAFKA_TOPIK, message.message)
    except Exception as ex:
        await producer.stop()
    return {'message': message.message}
