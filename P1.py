import serial
  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish


ser = serial.Serial('COM2', 9600, timeout=1)
while True:
    reading = ser.readline()
    print(reading)
    publish.single("slekin/qqq", reading, hostname="broker.hivemq.com")
