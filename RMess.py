# This is a messenger
from datetime import datetime
import requests
from PyQt5 import QtWidgets, QtCore

from clientui import Ui_MainWindow


class Rmess(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, url):  # initialization
        super().__init__()
        self.setupUi(self)
        self.after_timestamp = -1
        self.load_messages()
        # calls the function update_messages by timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

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
        response = None
        # to avoid problems when the server doesn't work
        try:
            response = requests.get(self.url + '/messages',
                                    params={'after_timestamp': self.after_timestamp})
        except SystemError:
            pass

        if response and response.status_code == 200:
            messages = response.json()['messages']
            for message in messages:
                self.pretty_print(message)
                self.after_timestamp = message['timestamp']
            return messages

    # calls update_messages that returns messages until it gets no messages
    # solves the problem of reducing the load on the messenger
    def load_messages(self):
        while self.update_messages():
            pass

    # when the button is pressed, message is send to the server
    def button_pressed(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        data = {'name': name, 'text': text}
        response = None

        try:
            response = requests.post(self.url + '/send', json=data)
        except SystemError:
            pass

        if response and response.status_code:
            self.textEdit.clear()
            self.textEdit.repaint()
        else:
            self.textBrowser.append('При отправке произошла ошибка')
            self.textBrowser.append('')
            self.textBrowser.repaint()


app = QtWidgets.QApplication([])
window = Rmess('http://127.0.0.1:5000')
window.show()
app.exec_()
