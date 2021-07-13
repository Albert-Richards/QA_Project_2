from flask import Flask, render_template, jsonify
import requests
# from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
# db = SQLAlchemy(app)


@app.route('/')
def home():
    species = requests.get('http://species_api:5000/get_species')
    class_ = requests.get('http://class_api:5000/get_class')
    stats = requests.post('http://stats_api:5000/get_stats', json = {"species":species.text, "class":class_.text})
    return render_template('index.html', species=species.text, class1=class_.text, stats = stats)
    print(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)