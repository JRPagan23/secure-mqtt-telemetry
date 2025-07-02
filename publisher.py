import ssl
import time
import json
import random
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet

# Load encryption key from file
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

key = load_key()
cipher_suite = Fernet(key)

# MQTT broker details
BROKER = "localhost"
PORT = 8884
TOPIC = "satellite/telemetry"

# TLS certificate files - update paths if needed
CA_CERT = "certs/ca.crt"
CLIENT_CERT = "certs/client.crt"
CLIENT_KEY = "certs/client.key"

def generate_telemetry():
    telemetry = {
        "temperature_celsius": round(random.uniform(50, 80), 2),
        "orientation_deg": {
            "pitch": round(random.uniform(-180, 180), 2),
            "yaw": round(random.uniform(-180, 180), 2),
            "roll": round(random.uniform(-180, 180), 2),
        },
        "battery_percent": round(random.uniform(20, 100), 2),
        "timestamp": time.time()
    }
    return telemetry

def main():
    client = mqtt.Client()

    client.tls_set(
        ca_certs=CA_CERT,
        certfile=CLIENT_CERT,
        keyfile=CLIENT_KEY,
        tls_version=ssl.PROTOCOL_TLSv1_2
    )

    client.connect(BROKER, PORT, 60)
    client.loop_start()
    print(f"Publishing encrypted telemetry to topic '{TOPIC}'...")

    try:
        while True:
            telemetry = generate_telemetry()
            telemetry_json = json.dumps(telemetry)
            encrypted_message = cipher_suite.encrypt(telemetry_json.encode())

            client.publish(TOPIC, encrypted_message)
            print(f"Encrypted telemetry sent: {telemetry}")

            time.sleep(5)  # Send every 5 seconds

    except KeyboardInterrupt:
        print("Stopping publisher...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
