import os, sys, datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# enable CORS to test with localhost api: http://localhost:1234
CORS(app)

TASK_LIST = [
    { 'id': 1, 'title': 'Task One' },
    { 'id': 2, 'title': 'Task Two' }
]

@app.route('/')
def welcome_to_simple_todo_api():
    return 'Hello, Welcome to Simple Todo API! (Using Flask)'

@app.route('/tasklist')
def get_task_list():
    return jsonify(TASK_LIST)

if __name__ == '__main__':
    app.run(host='localhost', port=1234)