from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# mongosh "mongodb+srv://cluster0.v4wppde.mongodb.net/myFirstDatabase" --apiVersion 1 --username shiyanboxer
# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client["quiz_results"]
collection = db["results"]

# API endpoint to save quiz results
@app.route('/quiz_results', methods=['POST'])
def save_quiz_results():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Quiz results saved successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
