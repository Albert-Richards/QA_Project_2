  
from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_stats', methods=['POST'])
def get_stats():
    stats={"Combat" : 5, "Biotic" : 5, "Tech" : 5}
    if data1 == "Turian":
        stats.update({"Combat": stats["Combat"]+1}, {"Biotic": stats["Biotic"]-2}, {"Tech": stats["Tech"]+1})
    elif data1 == "Salarian":
        stats.update({"Combat": stats["Combat"]-3}, {"Biotic": stats["Biotic"]+1}, {"Tech": stats["Tech"]+2})
    elif data1 == "Asari":
        stats.update({"Biotic": stats["Biotic"]+3}, {"Tech": stats["Tech"]-3})
    if data2 == "Adept":
        stats.update({"Biotic": stats["Biotic"]+4})
    elif data2 == "Engineer"
        stats.update({"Tech": stats["Tech"]+4})
    elif data2 == "Sentinel"
        stats.update({"Biotic": stats["Biotic"]+2}, {"Tech": stats["Tech"]+2})
    elif data2 == "Soldier":
        stats.update({"Combat": stats["Combat"]+4})
    elif data2 == "Vanguard":
        stats.update({"Combat": stats["Combat"]+2}, {"Biotic": stats["Biotic"]+2})
    elif data2 == "Infiltrator":
        stats.update({"Combat": stats["Combat"]+2}, {"Tech": stats["Tech"]+2})
    return stats

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)