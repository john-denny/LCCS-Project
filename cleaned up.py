from flask import Flask, jsonify, request
from flask_cors import CORS  
import serial
import time
import threading
from datetime import datetime


global score, shots, last_5_shots
score = shots = 0

last_5_shots = []

# Set the serial port and baud rate
ARDUINO_SERIAL_PORT = 'COM6'
MICROBIT_SERIAL_PORT = 'COM7'
MICROBIT_BAUD_RATE = 115200
ARDUINO_BAUD_RATE = 9600


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Open the serial port
arduino_ser = serial.Serial(ARDUINO_SERIAL_PORT, ARDUINO_BAUD_RATE, timeout=1)
microbit_ser = serial.Serial(MICROBIT_SERIAL_PORT, MICROBIT_BAUD_RATE, timeout=1)


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
            global shots, last_5_shots,score
            shots += 1
            current_score = score
            time.sleep(4) # Wait 4 seconds
            if current_score < score:
                print("Shot Has been made")
                last_5_shots.insert(0,{"result": "made"})
            else:
                print("Shot has been missed")
                last_5_shots.insert(0,{"result": "missed"})
            # Ensure we only deal with the last 5 shots
            if len(last_5_shots) > 5:
                list.pop()
                


def get_updated_data():
    global shots, score,last_5_shots
    shots_taken = shots
    shots_made = score
    shot_percentage = (shots_made / shots_taken) * 100 if shots_taken > 0 else 0

    return {
        "shotsTaken": shots_taken,
        "shotsMade": shots_made,
        "shotPercentage": round(shot_percentage, 2),
        "lastShots": last_5_shots
    }

# API endpoint to get shot statistics
@app.route('/api/shots', methods=['GET'])
def get_shot_statistics():
    return jsonify(get_updated_data())

@app.route('/api/username_happiness', methods=['POST'])
def store_username_happiness():
    data = request.get_json()

    with open("shooting_happiness.csv","a") as logfile:
        logfile.write(f"{data['username']}, {data['happiness']}, {datetime.now().strftime('%Y-%m-%d %H:%M')}, ")
    # Return a response, for example, a JSON response
    return '👍'

@app.route('/api/end_log', methods=['POST'])
def store_happiness_after():
    global shots, score, last_5_shots
    data = request.get_json()


    with open("shooting_happiness.csv","a") as logfile:
        logfile.write(f"{data['happiness']}, {shots}, {score}, {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    # Reset the results
    shots = score = 0
    last_5_shots = []
    return '👍'




if __name__ == '__main__':
    try:
        # Create threads for reading data
        arduino_thread = threading.Thread(target=read_arduino)
        microbit_thread = threading.Thread(target=read_microbit)

        # Start the threads
        arduino_thread.start()
        microbit_thread.start()

        # Runs the server on the main thread
        app.run()

    except KeyboardInterrupt:
        print(f"Shots taken: {shots} \nMade: {score}")
        print("Exiting...")

    finally:
        # Close the serial ports when the script is interrupted
        arduino_ser.close()
        microbit_ser.close()
