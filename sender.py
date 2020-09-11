# sends a POST request to the server
import requests

url = 'http://127.0.0.1:5000/send'

name = input('What\'s your name?: ')
while True:
    text = input()
    data = {'name': name, 'text': text}
    response = requests.post(url, json=data)  # sends a request to the server; sends a JSON data
