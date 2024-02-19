import serial
import time
import threading

global score
global shots
score = shots = 0


def read_arduino():
    while True:
        arduino_line = arduino_ser.readline().decode('utf-8').strip()
        if "1" in arduino_line:
            print("ARDUINO COMMS: ", arduino_line)
            global score
            score += 1
            time.sleep(1)

def read_microbit():
    while True:
        microbit_line = microbit_ser.readline().decode('utf-8').strip()
        if "1" in microbit_line:
            print("MICROBIT COMMS: ", microbit_line)
            global shots
            shots += 1
            time.sleep(1)
            # Your logic for Microbit data goes here

# Set the serial port and baud rate
arduino_serial_port = 'COM4'
arduino_baud_rate = 9600

microbit_serial_port = 'COM7'
microbit_baud_rate = 9600

# Open the serial port
arduino_ser = serial.Serial(arduino_serial_port, arduino_baud_rate, timeout=1)
microbit_ser = serial.Serial(microbit_serial_port, microbit_baud_rate, timeout=1)

try:
    # Create threads for reading data
    arduino_thread = threading.Thread(target=read_arduino)
    microbit_thread = threading.Thread(target=read_microbit)

    # Start the threads
    arduino_thread.start()
    microbit_thread.start()

    # Keep the main thread alive to handle KeyboardInterrupt
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print(f"Shots taken: {shots} \nMade: {score}")
    print("Exiting...")

finally:
    # Close the serial ports when the script is interrupted
    arduino_ser.close()
    microbit_ser.close()
