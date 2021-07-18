from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_species', methods=['GET'])
def get_species():
    return random.choice(['Human', 'Salarian', 'Turian', 'Asari'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)