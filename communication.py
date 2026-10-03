"""
This script establishes a serial connection with an Arduino device to monitor its heartbeat signal. If the Arduino disconnects or fails to send a heartbeat within the specified timeout, the script will lock the Windows PC as a security measure.
"""

import os
import time
import serial 

PORT = 'COM7' 
BAUD_RATE = 9600 
TIMEOUT_LIMIT = 3 

def lock_pc():
    print("Arduino disconnected! Locking Windows...")
    os.system('rundll32.exe user32.dll,LockWorkStation')

print(f"Starting Lock Daemon on {PORT}. Secure your Arduino...")

while True:
    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT_LIMIT) as arduino:
            # Give the Arduino 2 seconds to reboot after opening the port
            time.sleep(2)
            print("Link established. Monitoring heartbeat...")
            
            while True:
                raw_data = arduino.readline()
                payload = raw_data.decode('utf-8', errors='ignore').strip()
                
                if not payload:
                    lock_pc()
                    break
                    
                if payload == "DEVICE_ACTIVE":
                    print("Heartbeat verified: System Safe.")
                    
                time.sleep(0.1)

    except (serial.SerialException, PermissionError):
        lock_pc()
        print("Waiting for hardware re-insertion... Retrying in 3 seconds.")
        time.sleep(3)