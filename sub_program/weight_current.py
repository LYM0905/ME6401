import serial
import time

# Create a serial connection with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with your actual serial port
time.sleep(2)  # Wait for the connection to be established

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').rstrip()
            if "Weight Current:" in line:
                weight_current = float(line.split(":")[1])
                print("Current Weight:", weight_current)
except KeyboardInterrupt:
    ser.close()
