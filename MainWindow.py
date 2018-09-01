# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore
from PySide2.QtWidgets import\
    QApplication,\
    QWidget,\
    QLabel,\
    QStatusBar,\
    QVBoxLayout,\
    QSpacerItem,\
    QSizePolicy,\
    QGridLayout,\
    QPushButton,\
    QMainWindow,\
    QFileDialog

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
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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

        self.excelBtn.clicked.connect(self, QtCore.SLOT("onExcelBtnClicke()"))
        self.sqlBtn.clicked.connect(self, QtCore.SLOT("onsqlBtnClicke()"))

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.excelBtn.setText(_translate("MainWindow", "select exel file", None))
        self.sqlBtn.setText(_translate("MainWindow", "select sql file", None))


    def onExcelBtnClicke(self):
        out = QFileDialog.getOpenFileNames(self, 'Select excel file', './', 'Excel files (*.xls *.xlsx)')
        excelFile = out[0]
        self.excelLabel.setText(excelFile[0])
        print(excelFile)

    def onsqlBtnClicke(self):
        out = QFileDialog.getOpenFileNames(self, 'Select sql file', './', 'sql files (*.sqlite)')
        sqlFile = out[0]
        self.sqlLabel.setText(sqlFile[0])
        print(sqlFile)

