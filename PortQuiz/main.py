from PyQt5 import QtWidgets
import sys


class PortQuiz(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()

		self.setWindowTitle("Port Quiz")
		screen_resolution = app.desktop().screenGeometry()
		self.setGeometry(screen_resolution)
		self.show()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	w = PortQuiz()
	app.exec()
