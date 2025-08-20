import os
import random
import time
from cryptography.fernet import Fernet

# Configuration file for secure IoT device simulator

# IoT Device Settings
DEVICE_ID = "RKHJ-SECU-001"
DEVICE_NAME = "Smart Thermostat"

# Network Settings
NETWORK_INTERFACE = "eth0"
NETWORK_IP = "192.168.1.100"
NETWORK_MASK = "255.255.255.0"
NETWORK_GATEWAY = "192.168.1.1"

# Security Settings
ENCRYPTION_KEY = Fernet.generate_key()
AUTHENTICATION_TOKEN = os.urandom(16)

# Simulator Settings
SIMULATION_INTERVAL = 10  # seconds
SIMULATION_DATA = {
    "temperature": lambda: round(random.uniform(20, 25), 2),
    "humidity": lambda: round(random.uniform(40, 60), 2),
    "pressure": lambda: round(random.uniform(900, 1100), 2)
}

# Logging Settings
LOGGING_ENABLED = True
LOGGING_FILE = "device_log.txt"

# Simulation Functions
def generate_simulation_data():
    data = {}
    for sensor, func in SIMULATION_DATA.items():
        data[sensor] = func()
    return data

def encrypt_data(data):
    fernet = Fernet(ENCRYPTION_KEY)
    encrypted_data = fernet.encrypt(str(data).encode())
    return encrypted_data

def simulate_device():
    while True:
        data = generate_simulation_data()
        encrypted_data = encrypt_data(data)
        print(f"Device {DEVICE_ID} sending data: {encrypted_data}")
        time.sleep(SIMULATION_INTERVAL)

if __name__ == "__main__":
    simulate_device()