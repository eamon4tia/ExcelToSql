# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableTest.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PySide2 import QtCore, QtSql
from PySide2.QtCore import Qt, QObject
from PySide2 import QtCore
from PySide2.QtWidgets import\
    QApplication,\
    QWidget,\
    QLabel,\
    QLineEdit,\
    QStatusBar,\
    QVBoxLayout,\
    QSpacerItem,\
    QSizePolicy,\
    QGridLayout,\
    QPushButton,\
    QMainWindow,\
    QFileDialog

import sys

from PySide2.QtSql import *
from PySide2.QtSql import QSqlQueryModel

from PySide2.QtGui import QIcon, QPixmap


from PySide2.QtGui import QStandardItemModel, QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout, QStatusBar, QMainWindow, QTableWidgetItem, \
    QTableWidget, QHBoxLayout, QPushButton, QSpacerItem, QLineEdit, QSizePolicy, QLayout, QGridLayout, QDateEdit



import pandas as pd

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(565, 358)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchTE = QLineEdit(self.centralwidget)
        self.searchTE.setObjectName(_fromUtf8("searchTE"))
        self.horizontalLayout.addWidget(self.searchTE)
        self.searchBtn = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setStyleSheet(_fromUtf8("border: none"))
        self.searchBtn.setText(_fromUtf8(""))
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("../.designer/gitlab/ExcelToSql/icons/searchBtn.png")), QIcon.Normal,
                       QIcon.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setIconSize(QtCore.QSize(48, 24))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))

        self.horizontalLayout.addWidget(self.searchBtn)
        self.pushButton_2 = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButton_2.setStyleSheet(_fromUtf8("color: blue"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.horizontalLayout.addWidget(self.pushButton_2)
       # self.pushButton_2.clicked.connect(self.onRunBtnClick())

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout.addWidget(self.dateEdit_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidget = QTableWidget(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)


        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi()

        

        QtCore.QMetaObject.connectSlotsByName(self)
        print("A")
        self.pushButton_2.clicked.connect(self, QtCore.SLOT("onRunBtnClick()"))
        print("B")

        conn = sqlite3.connect("/home/eamon/Desktop/test.sqlite")
        result = conn.execute("SELECT * FROM Sheet1")
        for raw_number, raw_data in enumerate(result):
            self.tableWidget.insertRow(raw_number)
#            print(raw_number)
            for column_number, data in enumerate(raw_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(raw_number, column_number, item)
#                print("\t", column_number)




        conn.close()




    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost", None))

    def onRunBtnClick(self):

        db= sqlite3.connect("/home/eamon/Desktop/test.sqlite")
        cur = db.cursor()
        q = "SELECT * FROM Sheet1 WHERE name='%s'" % (self.searchTE.text(),)
        print(q)

        res = cur.execute(q)
        if res:
            self.tableWidget.clear()
            for raw_number, raw_data in enumerate(res):
                self.tableWidget.insertRow(raw_number)

                for column_number, data in enumerate(raw_data):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(raw_number, column_number, item)





app = QApplication()
ui = Ui_MainWindow()
ui.show()
sys.exit(app.exec_())


