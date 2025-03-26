import os
from dotenv import load_dotenv

load_dotenv()

HISTORY_FOLDER = os.getenv("HISTORY_FOLDER", "saved_images")
os.makedirs(HISTORY_FOLDER, exist_ok=True)

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "parking/gate/entry")
MQTT_MESSAGE = os.getenv("MQTT_MESSAGE", "open")
OCR_API_KEYS = os.getenv("OCR_API_KEYS", "").split(",")
