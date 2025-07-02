import ssl
import paho.mqtt.client as mqtt

# Broker connection settings
BROKER = "localhost"
PORT = 8884

# Paths to your certificate files — update these if needed!
CA_CERT = "/Users/jorgerodriguezpagan/Downloads/secure-mqtt-telemetry/certs/ca.crt"
CLIENT_CERT = "/Users/jorgerodriguezpagan/Downloads/secure-mqtt-telemetry/certs/client.crt"
CLIENT_KEY = "/Users/jorgerodriguezpagan/Downloads/secure-mqtt-telemetry/certs/client.key"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully!")
        client.subscribe("telemetry/#")  # subscribe to your topics
    else:
        print(f"Connect failed with result code {rc}")

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

def main():
    client = mqtt.Client()
    client.tls_set(ca_certs=CA_CERT,
                   certfile=CLIENT_CERT,
                   keyfile=CLIENT_KEY,
                   tls_version=ssl.PROTOCOL_TLSv1_2)
    
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Connecting to broker {BROKER} on port {PORT}...")
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()

