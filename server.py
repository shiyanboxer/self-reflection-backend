from flask import Flask, request, jsonify
from pymongo import MongoClient
import connection as connection


app = Flask(__name__)

# Connect to database
db = connection.connect_db()

# Making sure db is working
# @app.route('/', methods=['GET'])
# def hello_world():
#     db.insert_one({'email': 'shiyanboxer'})
#     return "Hello World"

# Save quiz results to database along with user's name and email
@app.route('/save', methods=['POST'])
def save_quiz_results():
    data = request.json
    db.insert_one(data)
    return jsonify({"message": "Quiz results saved successfully!"}), 201

# Retrieve quiz results for user given their email
@app.route('/retrieve', methods=['GET'])
def retrieve_quiz_results(email):
    user = db.find_one({'email': email})
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
