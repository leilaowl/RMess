# creates a server
import time
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
db = []


@app.route('/')
def main_page():
    return "WELCOME! This is RMess! <a href='/status'>Статус<a/>"


@app.route('/status')
def status():
    return {
        'status': True,
        'Name': 'RMess',
        'time': datetime.now()
     }


@app.route('/send', methods=['POST'])
def send():
    data = request.json  # to access incoming request data and reformat it to python object

    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': time.time()
    })
    return {'ok': True}


@app.route('/messages')
def messages():
    # 'request.args' gets the arguments
    if 'after_id' in request.args:
        after_id = int(request.args['after_id']) + 1
    else:
        after_id = 0
    return {'messages': db[after_id:]}


app.run()
