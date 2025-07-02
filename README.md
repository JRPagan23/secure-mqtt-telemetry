Secure MQTT Telemetry Simulator

This project simulates a secure satellite telemetry system using MQTT with TLS encryption.

 Summary

Publisher (Satellite): Generates encrypted telemetry data (temperature, orientation, battery).

Subscriber (Ground Station): Decrypts and displays real-time telemetry securely.

Broker: Mosquitto MQTT broker running on TLS (port 8884), secured with CA-signed certificates.

Encryption: AES encryption with a shared secret key (generated securely).

 Tech Stack

Python 3

paho-mqtt for MQTT communication

cryptography for secure key generation and encryption

Mosquitto MQTT Broker with TLS

Self-signed certificates for local encryption

 Project Structure

secure-mqtt-telemetry/
├── certs/                     # TLS certificates
│   ├── ca.crt
│   ├── server.crt
│   └── server.key
├── secret.key                 # AES encryption key
├── crypto_utils.py            # Crypto helper functions
├── publisher.py               # Simulates satellite
├── subscriber.py              # Simulates ground station
├── mosquitto_tls.conf         # Mosquitto broker TLS config
└── README.md

️ Usage

Start the broker:

mosquitto -c mosquitto_tls.conf

Run the subscriber (ground station):

python3 subscriber.py

Run the publisher (satellite):

python3 publisher.py

You should see real-time encrypted telemetry data being published and securely received.

️ Security Features

All MQTT traffic is encrypted using TLS (port 8884).

Data payloads are encrypted using AES symmetric encryption.

Certificates prevent unauthorized connections.

The secret AES key is not hardcoded but securely generated and stored.

 Use Cases

Demonstrates secure communication principles for IoT and aerospace.

Useful for cybersecurity and satellite systems portfolios.

Great interview project to showcase encryption, networking, and Python skills.

License

This project is for educational use only.


