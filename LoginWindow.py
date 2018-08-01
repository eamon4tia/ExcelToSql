# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class LoginWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)


    def onLoginBtnClicked(self):
        password = self.textEdit.toPlainText()
        if password == "Eamon":

            self.w = QtGui.QWidget()
            self.w.show()
            self.close()

            print('Login succsefully')
        else:
            print('wrong password')


    def setupUi(self):
        self.setObjectName(_fromUtf8("LoginWindow"))
        self.resize(526, 96)
        self.setStyleSheet(_fromUtf8("background-color:#333;"))

        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(50, 30, 311, 31))
        self.textEdit.setStyleSheet(_fromUtf8("QTextEdit{color: white}"))
        self.textEdit.setObjectName(_fromUtf8("password"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(390, 30, 99, 27))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {color:#FD670F}"))
        self.pushButton.setObjectName(_fromUtf8("login Button"))

        self.retranslateUi()
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onLoginBtnClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("LoginWindow", "LoginWindow", None))
        self.pushButton.setText(_translate("LoginWindow", "Login", None))

