
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'user-signups',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='email-consumer-group'
)

print("📥 Kafka Consumer started, listening to 'user-signups' topic...")

for message in consumer:
    email = message.value.decode('utf-8')
    print(f"📨 Received email: {email}")
