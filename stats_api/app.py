from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_stats', methods=['POST'])
def get_stats():
    data1 = str(request.get_json()["species"])
    data2 = str(request.get_json()["class"])
    stats={"Combat" : 5, "Biotic" : 5, "Tech" : 5}
    if data1 == "Turian":
        stats.update({"Combat": stats["Combat"]+1}) 
        stats.update({"Biotic": stats["Biotic"]-2})
        stats.update({"Tech": stats["Tech"]+1})
    elif data1 == "Salarian":
        stats.update({"Combat": stats["Combat"]-3})
        stats.update({"Biotic": stats["Biotic"]+1})
        stats.update({"Tech": stats["Tech"]+2})
    elif data1 == "Asari":
        stats.update({"Biotic": stats["Biotic"]+3})
        stats.update({"Tech": stats["Tech"]-3})
    if data2 == "Adept":
        stats.update({"Biotic": stats["Biotic"]+4})
    elif data2 == "Engineer":
        stats.update({"Tech": stats["Tech"]+4})
    elif data2 == "Sentinel":
        stats.update({"Biotic": stats["Biotic"]+2})
        stats.update({"Tech": stats["Tech"]+2})
    elif data2 == "Soldier":
        stats.update({"Combat": stats["Combat"]+4})
    elif data2 == "Vanguard":
        stats.update({"Combat": stats["Combat"]+2})
        stats.update({"Biotic": stats["Biotic"]+2})
    elif data2 == "Infiltrator":
        stats.update({"Combat": stats["Combat"]+2}) 
        stats.update({"Tech": stats["Tech"]+2})
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)