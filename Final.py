from builtins import print

from PySide2 import  QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def onExcelBtnClick(self):
        out = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select excel file', './', 'Excel files (*.xls *.xlsx)')
        excelFileNames = out[0]
        if len(excelFileNames) > 0:
            self.ui.excelFileName = excelFileNames[0]
            self.ui.excelLabel.setText(self.ui.excelFileName)
            if self.ui.sqlFileName is not None:
                self.ui.runBtn.setEnabled(True)

    def onSqlBtnClick(self):
        out = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select sql file', './', 'SQL files (*.sqlite *.sql *.db)')
        sqlFileNames = out[0]
        if len(sqlFileNames) > 0:
            self.sqlFileName = sqlFileNames[0]
            self.ui.sqlLabel.setText(self.sqlFileName)
            if self.ui.excelFileName is not None:
                self.ui.runBtn.setEnabled(True)

    def onRunBtnClick(self):

        from pandas import read_excel
        import sqlite3
        import numpy as np

        tableName = "Sheet1"

        xlsFile = read_excel(self.ui.excelFileName, tableName)

        columns = xlsFile.columns

        db = sqlite3.connect(self.ui.sqlFileName)
        cursor = db.cursor()

        # cursor.execute("DELETE FROM " + tableName)

        Ncolumns = len(columns)
        Nrows = len(xlsFile)

        query = "INSERT INTO " + tableName + " (id, name, cost , date) VALUES('{id}', '{name}', '{cost}','{date}')"

        print(Nrows)
        for i in range(1, Nrows):
            record = xlsFile.loc[i]

            q = query
            for column in columns:
                #print('.')
                data = record[column]
                if column == "id":
                    q3 = "SELECT cost FROM Sheet2 WHERE id=%s" % (data)
                    cursor.execute(q3)
                    y = cursor.fetchone()[0]
                    #print("cost",y)

                if column == "cost":
                    a = int(y)
                    b = int(data)
                    q1 = "UPDATE Sheet2 SET cost=%s WHERE id=%s" % ((a+b),data)

                    #print("q= "+ q1)
                    cursor.execute(q1)

                if type(data) == np.int64:
                    data = str(data)

                q = q.replace('{' + column + '}', data)
            cursor.execute(q)

        db.commit()



        db.close()
        print('Done')
        print(tableName)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(716, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.InsertTab = QtWidgets.QWidget()
        self.InsertTab.setObjectName(_fromUtf8("InsertTab"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InsertTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtWidgets.QSpacerItem(20, 109, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.insertGridLayout = QtWidgets.QGridLayout()
        self.insertGridLayout.setObjectName(_fromUtf8("insertGridLayout"))
        self.runBtn = QtWidgets.QPushButton(self.InsertTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        self.runBtn.setMouseTracking(False)
        self.runBtn.setAutoFillBackground(False)
        self.runBtn.setStyleSheet(_fromUtf8("border: none"))
        self.runBtn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runBtn.setIcon(icon)
        self.runBtn.setIconSize(QtCore.QSize(64, 64))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.insertGridLayout.addWidget(self.runBtn, 0, 3, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.insertGridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.excelLabel = QtWidgets.QLabel(self.InsertTab)
        self.excelLabel.setText(_fromUtf8(""))
        self.excelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.excelLabel.setObjectName(_fromUtf8("excelLabel"))
        self.insertGridLayout.addWidget(self.excelLabel, 1, 0, 1, 3)
        self.sqlBtn = QtWidgets.QPushButton(self.InsertTab)
        self.sqlBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.sqlBtn.setObjectName(_fromUtf8("sqlBtn"))
        self.insertGridLayout.addWidget(self.sqlBtn, 0, 4, 1, 1)
        self.excelBtn = QtWidgets.QPushButton(self.InsertTab)
        self.excelBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.excelBtn.setObjectName(_fromUtf8("excelBtn"))
        self.insertGridLayout.addWidget(self.excelBtn, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.insertGridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.sqlLabel = QtWidgets.QLabel(self.InsertTab)
        self.sqlLabel.setText(_fromUtf8(""))
        self.sqlLabel.setObjectName(_fromUtf8("sqlLabel"))
        self.insertGridLayout.addWidget(self.sqlLabel, 1, 4, 1, 2)
        self.verticalLayout_2.addLayout(self.insertGridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.InsertTab, _fromUtf8(""))
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName(_fromUtf8("searchTab"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.searchTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.searchGridLayout = QtWidgets.QGridLayout()
        self.searchGridLayout.setObjectName(_fromUtf8("searchGridLayout"))
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.searchGridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.searchLE = QtWidgets.QLineEdit(self.searchTab)
        self.searchLE.setObjectName(_fromUtf8("searchLE"))
        self.searchGridLayout.addWidget(self.searchLE, 0, 1, 1, 1)
        self.searchBtn = QtWidgets.QPushButton(self.searchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setStyleSheet(_fromUtf8("border: none"))
        self.searchBtn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/searchBtn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon1)
        self.searchBtn.setIconSize(QtCore.QSize(48, 24))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.searchGridLayout.addWidget(self.searchBtn, 0, 2, 1, 1)
        self.filterBtn = QtWidgets.QPushButton(self.searchTab)
        self.filterBtn.setStyleSheet(_fromUtf8("border: none"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/filter_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterBtn.setIcon(icon2)
        self.filterBtn.setObjectName(_fromUtf8("filterBtn"))
        self.searchGridLayout.addWidget(self.filterBtn, 0, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.searchGridLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.searchTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.searchTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.excelBtn.clicked.connect(MainWindow, QtCore.SLOT("onExcelBtnClick()"))
        self.sqlBtn.clicked.connect(MainWindow, QtCore.SLOT("onSqlBtnClick()"))
        self.runBtn.clicked.connect(MainWindow, QtCore.SLOT("onRunBtnClick()"))

        self.excelFileName = None
        self.sqlFileName = "/home/eamon/Desktop/test.sqlite"
        self.sqlLabel.setText(self.sqlFileName)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Search</span></p></body></html>", None))
        self.sqlBtn.setText(_translate("MainWindow", "select sql file", None))
        self.excelBtn.setText(_translate("MainWindow", "select exel file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InsertTab), _translate("MainWindow", "INSERT", None))
        self.searchLE.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.filterBtn.setText(_translate("MainWindow", "Filter", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), _translate("MainWindow", "Search", None))

