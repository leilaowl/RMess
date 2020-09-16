# This is a messenger
from datetime import datetime
import requests
from PyQt5 import QtWidgets, QtCore

from clientui import Ui_MainWindow


class Rmess(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, url):  # initialization
        super().__init__()
        self.setupUi(self)

        self.after_id = -1
        # calls the function update_messages by timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

        # something
        self.url = url
        self.pushButton.pressed.connect(self.button_pressed)

    def pretty_print(self, text_message):
        """
        2020/09/08 10:00:23  Chandler
        Hi Monica!

        """
        dt = datetime.fromtimestamp(text_message['timestamp'])
        dt = dt.strftime('%Y/%m/%d %I:%M:%S %p')
        first_line = dt + '  ' + text_message['name']
        self.textBrowser.append(first_line)
        self.textBrowser.append(text_message['text'])
        self.textBrowser.append('')
        self.textBrowser.repaint()

    def update_messages(self):
        response = requests.get(self.url + '/messages',
                                params={'after_id': self.after_id})
        messages = response.json()['messages']
        for message in messages:
            self.pretty_print(message)
            self.after_id = message['id']

    # when the button is pressed, message is send to the server
    def button_pressed(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        data = {'name': name, 'text': text}
        response = requests.post(self.url + '/send', json=data)
        self.textEdit.clear()
        self.textEdit.repaint()


app = QtWidgets.QApplication([])
window = Rmess('http://127.0.0.1:5000')
window.show()
app.exec_()
