# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OneForeAll.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore
from PySide2.QtWidgets import \
    QApplication, \
    QWidget, \
    QLabel, \
    QLineEdit, \
    QStatusBar, \
    QVBoxLayout, \
    QSpacerItem, \
    QSizePolicy, \
    QGridLayout, \
    QPushButton, \
    QMainWindow, \
    QFileDialog, QTabWidget

from PySide2.QtSql import QSqlQueryModel

from PySide2.QtGui import QIcon, QPixmap
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

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(651, 280)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 521, 361))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Insert = QWidget()
        self.Insert.setObjectName(_fromUtf8("Insert"))
        self.layoutWidget_2 = QWidget(self.Insert)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 100, 504, 76))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.excelBtn = QPushButton(self.layoutWidget_2)
        self.excelBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.excelBtn.setObjectName(_fromUtf8("excelBtn"))
        self.gridLayout.addWidget(self.excelBtn, 0, 1, 1, 1)
        self.excelLabel = QLabel(self.layoutWidget_2)
        self.excelLabel.setText(_fromUtf8(""))
        self.excelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.excelLabel.setObjectName(_fromUtf8("excelLabel"))
        self.gridLayout.addWidget(self.excelLabel, 1, 0, 1, 2)
        self.sqlBtn = QPushButton(self.layoutWidget_2)
        self.sqlBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.sqlBtn.setObjectName(_fromUtf8("sqlBtn"))
        self.gridLayout.addWidget(self.sqlBtn, 0, 3, 1, 1)
        self.runBtn = QPushButton(self.layoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        self.runBtn.setMouseTracking(False)
        self.runBtn.setAutoFillBackground(False)
        self.runBtn.setStyleSheet(_fromUtf8("background: transparent;"))
        self.runBtn.setText(_fromUtf8(""))
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("icons/run.png")), QIcon.Normal, QIcon.Off)
        self.runBtn.setIcon(icon)
        self.runBtn.setIconSize(QtCore.QSize(64, 64))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.gridLayout.addWidget(self.runBtn, 0, 2, 2, 1)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        
        
        self.tabWidget_2 = QTabWidget(self.Insert)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, -40, 521, 361))
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget_3 = QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 100, 504, 76))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.excelBtn_2 = QPushButton(self.layoutWidget_3)
        self.excelBtn_2.setMinimumSize(QtCore.QSize(200, 0))
        self.excelBtn_2.setObjectName(_fromUtf8("excelBtn_2"))
        self.gridLayout_3.addWidget(self.excelBtn_2, 0, 1, 1, 1)
        self.excelLabel_2 = QLabel(self.layoutWidget_3)
        self.excelLabel_2.setText(_fromUtf8(""))
        self.excelLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.excelLabel_2.setObjectName(_fromUtf8("excelLabel_2"))
        self.gridLayout_3.addWidget(self.excelLabel_2, 1, 0, 1, 2)
        self.sqlBtn_2 = QPushButton(self.layoutWidget_3)
        self.sqlBtn_2.setMinimumSize(QtCore.QSize(200, 0))
        self.sqlBtn_2.setObjectName(_fromUtf8("sqlBtn_2"))
        self.gridLayout_3.addWidget(self.sqlBtn_2, 0, 3, 1, 1)
        self.runBtn_2 = QPushButton(self.layoutWidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn_2.sizePolicy().hasHeightForWidth())
        self.runBtn_2.setSizePolicy(sizePolicy)
        self.runBtn_2.setMouseTracking(False)
        self.runBtn_2.setAutoFillBackground(False)
        self.runBtn_2.setStyleSheet(_fromUtf8("background: transparent;"))
        self.runBtn_2.setText(_fromUtf8(""))
        self.runBtn_2.setIcon(icon)
        self.runBtn_2.setIconSize(QtCore.QSize(64, 64))
        self.runBtn_2.setObjectName(_fromUtf8("runBtn_2"))
        self.gridLayout_3.addWidget(self.runBtn_2, 0, 2, 2, 1)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 4, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.layoutWidget_4 = QWidget(self.tab_4)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 10, 541, 29))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.searchTE_2 = QLineEdit(self.layoutWidget_4)
        self.searchTE_2.setObjectName(_fromUtf8("searchTE_2"))
        self.horizontalLayout_2.addWidget(self.searchTE_2)
        self.pushButton_3 = QPushButton(self.layoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButton_3.setStyleSheet(_fromUtf8("color: blue"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.searchBtn_2 = QPushButton(self.layoutWidget_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn_2.sizePolicy().hasHeightForWidth())
        self.searchBtn_2.setSizePolicy(sizePolicy)
        self.searchBtn_2.setStyleSheet(_fromUtf8("border: none"))
        self.searchBtn_2.setText(_fromUtf8(""))
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8("../../.designer/gitlab/ExcelToSql/icons/searchBtn.png")), QIcon.Normal, QIcon.Off)
        self.searchBtn_2.setIcon(icon1)
        self.searchBtn_2.setIconSize(QtCore.QSize(48, 24))
        self.searchBtn_2.setObjectName(_fromUtf8("searchBtn_2"))
        self.horizontalLayout_2.addWidget(self.searchBtn_2)
        self.tableWidget_2 = QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 50, 541, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tabWidget.addTab(self.Insert, _fromUtf8(""))
        self.Search = QWidget()
        self.Search.setObjectName(_fromUtf8("Search"))
        self.layoutWidget = QWidget(self.Search)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 541, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.searchTE = QLineEdit(self.layoutWidget)
        self.searchTE.setObjectName(_fromUtf8("searchTE"))
        self.horizontalLayout.addWidget(self.searchTE)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButton_2.setStyleSheet(_fromUtf8("color: blue"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.searchBtn = QPushButton(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setStyleSheet(_fromUtf8("border: none"))
        self.searchBtn.setText(_fromUtf8(""))
        self.searchBtn.setIcon(icon1)
        self.searchBtn.setIconSize(QtCore.QSize(48, 24))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.horizontalLayout.addWidget(self.searchBtn)
        self.tableWidget = QTableWidget(self.Search)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 541, 271))
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
        self.tabWidget.addTab(self.Search, _fromUtf8(""))
        self.tab = QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)


        print('ABC')
        self.excelBtn.clicked.connect(self, QtCore.SLOT("onExcelBtnClick()"))
        self.sqlBtn.clicked.connect(self, QtCore.SLOT("onSqlBtnClick()"))
        self.runBtn.clicked.connect(self, QtCore.SLOT("onRunBtnClick()"))

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Search</span></p></body></html>", None))
        self.excelBtn.setText(_translate("MainWindow", "select exel file", None))
        self.sqlBtn.setText(_translate("MainWindow", "select sql file", None))
        self.tabWidget_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Search</span></p></body></html>", None))
        self.excelBtn_2.setText(_translate("MainWindow", "select exel file", None))
        self.sqlBtn_2.setText(_translate("MainWindow", "select sql file", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Insert", None))
        self.searchTE_2.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.pushButton_3.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Insert), _translate("MainWindow", "INSERT", None))
        self.searchTE.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.pushButton_2.setText(_translate("MainWindow", "...", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Search), _translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ADVANCET SERCH", None))

    def onExcelBtnClick(self):
        print('onExcelBtnClick')
        out = QFileDialog.getOpenFileNames(self, 'Select excel file', './', 'Excel files (*.xls *.xlsx)')
        excelFileNames = out[0];
        if len(excelFileNames) > 0:
            self.excelFileName = excelFileNames[0]
            self.excelLabel.setText(self.excelFileName)
            if self.sqlFileName is not None:
                self.runBtn.setEnabled(True)

    def onSqlBtnClick(self):
        print('onExcelBtnClick')

        out = QFileDialog.getOpenFileNames(self, 'Select sql file', './', 'SQL files (*.sqlite *.sql *.db)')
        sqlFileNames = out[0];
        if len(sqlFileNames) > 0:
            self.sqlFileName = sqlFileNames[0]
            self.sqlLabel.setText(self.sqlFileName)
            if self.excelFileName is not None:
                self.runBtn.setEnabled(True)

    def onRunBtnClick(self):
        print('onExcelBtnClick')

        from pandas import read_excel
        import sqlite3
        import sys
        import numpy as np
        print("Q")
        tableName = "Sheet1"
        #
        # def getUsage():
        #     return "Usage: ExcelToSql -i '/home/eamon/Desktop/test.xlsx' -o '/home/eamon/Desktop/test.sqlite'"
        #
        # def printUsage():
        #     print(getUsage())
        #
        # def checkUsage(argv):
        #     if len(argv) is not 5:
        #         printUsage()
        #         exit(-1)
        #
        #     for i in [1, 3]:
        #         option = argv[i].capitalize()
        #         if option == '-i':
        #             excelFilename = argv[i+1];
        # id
        #             if not (excelFilename.endswith('.xls') or excelFilename.endswith('.xlsx')):
        #                 print('Wrong excel file.')
        #                 exit(-1)
        #
        #         elif option == '-o':
        #             sqliteDBFilename = argv[i+1];
        #
        #             if not (sqliteDBFilename.endswith('.sql') or sqliteDBFilename.endswith('.sqlite') or sqliteDBFilename.endswith('.db')):
        #                 print("Error sqlite filename")
        #                 exit(-1);
        #
        #     return (excelFilename, sqliteDBFilename)
        #
        # excelFilename, sqliteDBFilename = checkUsage(sys.argv);
        #
        # print(excelFilename, sqliteDBFilename)

        xlsFile = read_excel(self.excelFileName, tableName)

        columns = xlsFile.columns

        db = sqlite3.connect(self.sqlFileName)
        cursor = db.cursor()

        # cursor.execute("DELETE FROM " + tableName)

        Ncolumns = len(columns)
        Nrows = len(xlsFile)

        query = "INSERT INTO " + tableName + " (id, name, cost , date) VALUES('{id}', '{name}', '{cost}','{date}')"

        for i in range(1, Nrows):
            record = xlsFile.loc[i]

            q = query
            for column in columns:
                # print('.')
                data = record[column]
                if column == "id":
                    # print("waw")
                    # print(data)
                    for column in columns:
                        data2 = record[column]
                        q3 = "SELECT cost FROM Sheet2  WHERE id=%s" % (data)
                        cursor.execute(q3)
                        y = cursor.fetchone()[0]
                        # print("cost",y)

                        cursor.execute(q3)
                        # print("=",q3)
                        if column == "cost":
                            # print("waw")

                            a = (int(y))
                            b = (int(data2))
                            # print(type(b))
                            q1 = "UPDATE Sheet2 SET cost=%s WHERE id=%s" % ((a + b), data)

                    # print("q= "+ q1)
                    cursor.execute(q1)

                if type(data) == np.int64:
                    data = str(data)

                q = q.replace('{' + column + '}', data)
            cursor.execute(q)

        db.commit()

        db.close()
        print('Done')
        print(tableName)
