import requests
from kafka import KafkaProducer
import json
import time


# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# OpenWeatherMap API endpoint and key
api_key = ''  # Replace with your actual API key
city = 'Johannesburg'  # Change to the city of your choice
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Function to fetch data from the API
def fetch_data_from_api():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Assuming the API returns JSON data
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None

# Produce messages
while True:
    data = fetch_data_from_api()
    if data:
        producer.send('weather_topic', value=data)  # Send to 'weather_topic'
        print(f"Produced: {data}")
    time.sleep(600)  # Fetch and send data every 10 minutes (600 seconds)

producer.flush()
producer.close()
