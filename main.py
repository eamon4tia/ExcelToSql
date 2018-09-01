import sys
from PySide2.QtWidgets import QApplication
from OmeForeAll import MainWindow

app = QApplication(sys.argv)

# window = LoginWindow();
OneForeAll = MainWindow()
OneForeAll.show()

sys.exit(app.exec_())

