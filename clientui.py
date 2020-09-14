# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 613)
        MainWindow.setStyleSheet("background-color: rgb(175, 202, 158);\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QTextEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"  background-color: PapayaWhip;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: DarkSalmon;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: IndianRed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: LightSalmon;\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 90, 361, 421))
        self.textBrowser.setStyleSheet("QTextEdit{\n"
"  background-color: Snow;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: Snow;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"  background-color: Snow;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: DarkSalmon;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: IndianRed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: LightSalmon;\n"
"}\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 530, 291, 41))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"  background-color: PapayaWhip;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: DarkSalmon;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: IndianRed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: LightSalmon;\n"
"}\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 530, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QTextEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"  background-color: PapayaWhip;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: DarkSalmon;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: IndianRed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: LightSalmon;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 60, 111, 21))
        self.lineEdit.setStyleSheet("QTextEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"  background-color: PapayaWhip;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: DarkSalmon;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: IndianRed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: LightSalmon;\n"
"}\n"
"\n"
"")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 63, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QTextEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  background-color: white;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"  background-color: PapayaWhip;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: DarkSalmon;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: IndianRed;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: LightSalmon;\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RMess"))
        self.label.setText(_translate("MainWindow", "RMess"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter your text..."))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label_2.setText(_translate("MainWindow", "Your name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
