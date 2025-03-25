import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD


def publish(topic: str, message: str):
    try:
        client = mqtt.Client()
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.connect(MQTT_BROKER, MQTT_PORT, 5)
        client.publish(topic, message)
        client.disconnect()
    except Exception as e:
        print(f"[MQTT] Failed to publish: {e}")
