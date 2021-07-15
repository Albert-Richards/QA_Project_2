  
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_stats', methods=['POST'])
def get_stats():
    data1 = str(request.get_json()["species"])
    data2 = str(request.get_json()["class"])
    stats={"Combat" : 5, "Biotic" : 5, "Tech" : 5}
    if data1 == "Quarian": 
        stats.update({"Biotic": stats["Biotic"]-3})
        stats.update({"Tech": stats["Tech"]+3})
    elif data1 == "Krogan":
        stats.update({"Combat": stats["Combat"]+3})
        stats.update({"Tech": stats["Tech"]-3})
    elif data1 == "Drell":
        stats.update({"Combat": stats["Combat"]-2})
        stats.update({"Biotic": stats["Biotic"]+1})
        stats.update({"Tech": stats["Tech"]+1})
    if data2 == "Bastion":
        stats.update({"Biotic": stats["Biotic"]+6})
        stats.update({"Tech": stats["Tech"]+2})
    elif data2 == "Operative":
        stats.update({"Tech": stats["Tech"]+6})
        stats.update({"Combat": stats["Combat"]+2})
    elif data2 == "Nemesis":
        stats.update({"Biotic": stats["Biotic"]+6})
        stats.update({"Combat": stats["Combat"]+2})
    elif data2 == "Commando":
        stats.update({"Combat": stats["Combat"]+6})
        stats.update({"Tech": stats["Tech"]+2})
    elif data2 == "Shock Trooper":
        stats.update({"Combat": stats["Combat"]+6})
        stats.update({"Biotic": stats["Biotic"]+2})
    elif data2 == "Medic":
        stats.update({"Biotic": stats["Biotic"]+2}) 
        stats.update({"Tech": stats["Tech"]+6})
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)