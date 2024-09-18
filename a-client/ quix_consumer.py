import quixstreams as qx

# Initialize the KafkaStreamingClient
client = qx.KafkaStreamingClient("localhost:9093")

# Create a topic consumer
topic_consumer = client.create_topic_consumer("my_topic")

# Define a callback to process messages
def on_message(message):
    print(f"Consumed: {message.value}")

# Subscribe to the topic and register the callback
topic_consumer.subscribe(on_message)

# Keep the script running
import time
while True:
    time.sleep(1)
