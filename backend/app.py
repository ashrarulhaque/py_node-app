from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os
import traceback

app = Flask(__name__)
CORS(app)

MONGO_URI = os.environ.get("MONGO_URI")
print(MONGO_URI)

client = None
collection = None

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client["flask_app"]
    collection = db["project_1"]

mockDB = []

@app.route("/submitform", methods=["POST"])
def submitform():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            return jsonify({"message": "Email and Name are required!"}), 400

        if collection is not None:
            collection.insert_one({"name": name, "email": email})
        else:
            mockDB.append({"name": name, "email": email})


        return jsonify({"message": "Data submitted successfully"}), 200
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
