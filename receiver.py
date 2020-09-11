# get a data from the server
from datetime import datetime
import time
import requests


def pretty_print(text_message):
    """
    2020/09/08 10:00:23  Chandler
    Hi Monica!

    """
    dt = datetime.fromtimestamp(text_message['timestamp'])
    dt = dt.strftime('%Y/%m/%d %I:%M:%S %p')
    first_line = dt + '  ' + text_message['name']
    print(first_line)
    print(text_message['text'])
    print()


url = 'http://127.0.0.1:5000/messages'
after_id = -1  # the identifier by which messages are filtered

while True:
    # asks for the messages, 'params' passes the arguments as a dictionary
    response = requests.get(url, params={'after_id': after_id})
    # prints new messages to the console one at a time
    messages = response.json()['messages']
    for message in messages:
        pretty_print(message)
        after_id = message['id']  # the last id of the printed message is assigned
    # pauses code execution
    # if there are already messages on the server, then the request is made immediately and does not wait
    if not messages:
        time.sleep(1)
