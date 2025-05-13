from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)  
load_dotenv()

mongo_url = os.getenv("Mongo_URL")
client = MongoClient(mongo_url)
db = client['taskdb']
collection = db['tasks']

if collection.count_documents({}) == 0:
    collection.insert_many([
        {"id": 1, "task": "Read code"},
        {"id": 2, "task": "Test API"},
        {"id": 3, "task": "Fill the form"}
    ])

@app.route('/api/tasks', methods=['GET'])

def get_tasks():
    tasks = list(collection.find({}, {'_id': 0}))
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
