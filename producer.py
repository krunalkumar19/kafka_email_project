
from kafka import KafkaProducer

# Setup Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'user-signups'

print("📤 Kafka Producer started. Type an email and press Enter to send. Type 'exit' to quit.")

while True:
    email = input("Enter email: ").strip()

    if email.lower() == 'exit':
        print("🛑 Exiting producer.")
        break

    if '@' not in email or '.' not in email:
        print("❌ Invalid email format. Try again.")
        continue

    # Save to file
    with open("emails.txt", "a") as f:
        f.write(email + "\n")

    # Send to Kafka topic
    producer.send(topic, email.encode('utf-8'))
    print(f"✅ Sent and saved: {email}")
