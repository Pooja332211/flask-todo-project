from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify({"message": "Hello from Flask!"})

# New route for To-Do items
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.form
    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }
    collection.insert_one(item)
    return jsonify({"status": "success", "item": item})

if __name__ == '__main__':
    app.run(debug=True)
