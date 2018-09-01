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

from PySide2.QtSql import QSqlQueryModel

from PySide2.QtGui import QIcon, QPixmap


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
        self.setMinimumSize(QtCore.QSize(0, 250))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectNasqlBtnme(_fromUtf8("centralwidget"))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.excelBtn = QPushButton(self.centralwidget)
        self.excelBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.excelBtn.setObjectName(_fromUtf8("excelBtn"))
        self.gridLayout.addWidget(self.excelBtn, 0, 1, 1, 1)
        self.sqlBtn = QPushButton(self.centralwidget)
        self.sqlBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.sqlBtn.setObjectName(_fromUtf8("sqlBtn"))
        self.gridLayout.addWidget(self.sqlBtn, 0, 3, 1, 1)
        self.runBtn = QPushButton(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        self.runBtn.setEnabled(False)
        self.runBtn.setMouseTracking(False)
        self.runBtn.setAutoFillBackground(False)
        self.runBtn.setStyleSheet(_fromUtf8("border: none;"))
        self.runBtn.setText(_fromUtf8(""))
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("icons/run.png")), QIcon.Normal, QIcon.Off)
        self.runBtn.setIcon(icon)
        self.runBtn.setIconSize(QtCore.QSize(64, 64))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.gridLayout.addWidget(self.runBtn, 0, 2, 2, 1)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.sqlLabel = QLabel(self.centralwidget)
        self.sqlLabel.setText(_fromUtf8(""))
        self.sqlLabel.setObjectName(_fromUtf8("sqlLabel"))
        self.gridLayout.addWidget(self.sqlLabel, 1, 3, 1, 2)
        self.excelLabel = QLabel(self.centralwidget)
        self.excelLabel.setText(_fromUtf8(""))
        self.excelLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.excelLabel.setObjectName(_fromUtf8("excelLabel"))
        self.gridLayout.addWidget(self.excelLabel, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.excelFileName = None
        self.sqlFileName = "/home/eamon/Desktop/test.sqlite"
        self.sqlLabel.setText(self.sqlFileName)

        self.excelBtn.clicked.connect(self, QtCore.SLOT("onExcelBtnClick()"))
        self.sqlBtn.clicked.connect(self, QtCore.SLOT("onSqlBtnClick()"))
        self.runBtn.clicked.connect(self,QtCore.SLOT("onRunBtnClick()"))

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.excelBtn.setText(_translate("MainWindow", "select exel file", None))
        self.sqlBtn.setText(_translate("MainWindow", "select sql file", None))


    def onExcelBtnClick(self):
        out = QFileDialog.getOpenFileNames(self, 'Select excel file', './', 'Excel files (*.xls *.xlsx)')
        excelFileNames = out[0];
        if len(excelFileNames) > 0:
            self.excelFileName = excelFileNames[0]
            self.excelLabel.setText(self.excelFileName)
            if self.sqlFileName is not None:
                self.runBtn.setEnabled(True)

    def onSqlBtnClick(self):
        out = QFileDialog.getOpenFileNames(self, 'Select sql file', './', 'SQL files (*.sqlite *.sql *.db)')
        sqlFileNames = out[0];
        if len(sqlFileNames) > 0:
            self.sqlFileName = sqlFileNames[0]
            self.sqlLabel.setText(self.sqlFileName)
            if self.excelFileName is not None:
                self.runBtn.setEnabled(True)

    def onRunBtnClick(self):

        from pandas import read_excel
        import sqlite3
        import sys
        import numpy as np

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
        #id
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
                #print('.')
                data = record[column]
                if column == "id":
                    #print("waw")
                    #print(data)
                    for column in columns:
                        data2 = record[column]
                        q3="SELECT cost FROM Sheet2  WHERE id=%s" % (data)
                        cursor.execute(q3)
                        y = cursor.fetchone()[0]
                        #print("cost",y)

                        cursor.execute(q3)
                        #print("=",q3)
                        if column == "cost":
                            #print("waw")

                            a= (int(y))
                            b=(int(data2))
                            #print(type(b))
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



class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)


    def onLoginBtnClickd(self):
        password = self.textEdit.toPlainText()
        if password == "Eamon":

            self.w = QWidget()
            self.w.show()
            self.close()

            print('Login succsefully')
        else:
            print('wrong password')


    def setupUi(self):
        self.setObjectName(_fromUtf8("LoginWindow"))
        self.resize(526, 96)
        self.setStyleSheet(_fromUtf8("background-color:#333;"))

        self.textEdit = QLineEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(50, 30, 311, 31))
        self.textEdit.setStyleSheet(_fromUtf8("QTextEdit{color: white}"))
        self.textEdit.setObjectName(_fromUtf8("password"))
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(390, 30, 99, 27))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {color:#FD670F}"))
        self.pushButton.setObjectName(_fromUtf8("login Button"))

        self.retranslateUi()
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.onLoginBtnClickd)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("LoginWindow", "LoginWindow", None))
        self.pushButton.setText(_translate("LoginWindow", "Login", None))

