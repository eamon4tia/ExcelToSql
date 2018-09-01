# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(651, 280)
        MainWindow.setMinimumSize(QtCore.QSize(0, 250))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.sqlLabel = QtGui.QLabel(self.centralwidget)
        self.sqlLabel.setText(_fromUtf8(""))
        self.sqlLabel.setObjectName(_fromUtf8("sqlLabel"))
        self.gridLayout.addWidget(self.sqlLabel, 1, 3, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.excelBtn = QtGui.QPushButton(self.centralwidget)
        self.excelBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.excelBtn.setObjectName(_fromUtf8("excelBtn"))
        self.gridLayout.addWidget(self.excelBtn, 0, 1, 1, 1)
        self.excelLabel = QtGui.QLabel(self.centralwidget)
        self.excelLabel.setText(_fromUtf8(""))
        self.excelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.excelLabel.setObjectName(_fromUtf8("excelLabel"))
        self.gridLayout.addWidget(self.excelLabel, 1, 0, 1, 2)
        self.sqlBtn = QtGui.QPushButton(self.centralwidget)
        self.sqlBtn.setMinimumSize(QtCore.QSize(200, 0))
        self.sqlBtn.setObjectName(_fromUtf8("sqlBtn"))
        self.gridLayout.addWidget(self.sqlBtn, 0, 3, 1, 1)
        self.runBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        self.runBtn.setMouseTracking(False)
        self.runBtn.setAutoFillBackground(False)
        self.runBtn.setStyleSheet(_fromUtf8("background: transparent;"))
        self.runBtn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runBtn.setIcon(icon)
        self.runBtn.setIconSize(QtCore.QSize(64, 64))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.gridLayout.addWidget(self.runBtn, 0, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.excelBtn.setText(_translate("MainWindow", "select exel file", None))
        self.sqlBtn.setText(_translate("MainWindow", "select sql file", None))

