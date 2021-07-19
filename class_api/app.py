
from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_class', methods=['GET'])
def get_class():
    return random.choice(['Nemesis', 'Bastion', 'Commando', 'Shock Trooper', 'Operative', 'Medic'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)