from flask import Flask, jsonify
from flask_cors import CORS  
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy shot data for demonstration
def get_updated_data():
    shots_taken = random.randint(100, 200)
    shots_made = random.randint(50, shots_taken)
    shot_percentage = (shots_made / shots_taken) * 100 if shots_taken > 0 else 0

    last_shots = [{"result": "made"},{"result" : "missed"}]

    return {
        "shotsTaken": shots_taken,
        "shotsMade": shots_made,
        "shotPercentage": round(shot_percentage, 2),
        "lastShots": last_shots
    }

# API endpoint to get shot statistics
@app.route('/api/shots', methods=['GET'])
def get_shot_statistics():
    return jsonify(get_updated_data())

@app.route('/api/name_hapiness')

if __name__ == '__main__':
    app.run(debug=True)
