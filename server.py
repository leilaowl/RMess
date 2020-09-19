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
        'time': datetime.now(),
        'messages_on_server': len(db),
        # the length of the set consisting of unique names, that is, the number of users on the server
        'users_on_server': len(set(message['name'] for message in db))
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
    if 'after_timestamp' in request.args:
        after_timestamp = float(request.args['after_timestamp'])
    else:
        after_timestamp = 0

    # pagination that helps us not to receive all messages at once in the receiver.py, but to receive them in parts.
    # if the timestamp from the server is bigger than a timestamp from the client, after_id = 0
    limit = 50
    after_id = 0
    for message in db:
        if message['timestamp'] > after_timestamp:
            break
        after_id += 1

    return {'messages': db[after_id:after_id+limit]}


app.run()
