from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Allows requests from JavaScript

JSON_FILE = "intents.json"

@app.route("/add_intent", methods=["POST"])
def add_intent():
    try:
        new_intent = request.get_json()

        with open(JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        data["intents"].append(new_intent)  # Add new intent

        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return jsonify({"message": "Intent added successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Send back error message
@app.route("/",methods=["GET"])
def main():
    return jsonify({"status": "Running on port 5500"})
if __name__ == "__main__":
    app.run(debug=True, port=5500)
