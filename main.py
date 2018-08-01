import sys
from PyQt4 import QtCore, QtGui
from LoginWindow import LoginWindow







app = QtGui.QApplication(sys.argv)

window = LoginWindow();
window.setupUi()
window.show()

sys.exit(app.exec_())

