from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from gui.mainwindow import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())
