import sys

from PySide2.QtCore import QCoreApplication, QObject, QUrl, Qt, SLOT, SIGNAL, QDate
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout
from PySide2.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine, QQmlApplicationEngine
from QtDatePicker.DatePicker import DatePicker


QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
app = QApplication(sys.argv)
w = QWidget()
w.setFixedSize(640, 480)
w.setLayout(QHBoxLayout())

datePicker = DatePicker()

def eamon():
    date = datePicker.selectedDate()
    print(date.year() + "/" + date.month() + "/" + date.day())

datePicker.selectionChanged.connect(eamon)
w.layout().addWidget(datePicker)
w.show()

sys.exit(app.exec_())