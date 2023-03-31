import random

from PyQt5 import QtWidgets, uic
import sys

from PortQuiz import PortQuizAwards, PortDictInformation

#https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/#importing-the-ui-file-in-python
class PortQuiz(QtWidgets.QMainWindow):
    def __init__(self):
        super(PortQuiz, self).__init__()
        uic.loadUi('PortQuizGame.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = PortQuiz()
app.exec_()

