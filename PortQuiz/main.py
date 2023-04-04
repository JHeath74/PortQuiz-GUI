import sys


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QPlainTextEdit
from PyQt5.QtCore import pyqtSlot

from PortQuiz.PortQuizProgram import PortQuizProgram


class PortQuiz(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Port Quiz'

		self.setFixedHeight(700)
		self.setFixedWidth(1300)
		self.initUI()
		PortQuizProgram.PortQuiz(self)

	def initUI(self):
		self.setWindowTitle(self.title)

		# Width,  then Height

		Port1 = QPushButton('Port 1:', self)
		Port1.setToolTip('Answer Choice 1')
		Port1.move(50, 500)
		Port1.resize(200, 100)
		Port1.clicked.connect(self.Port_1_on_click)

		Port2 = QPushButton('Port 2:', self)
		Port2.setToolTip('Answer Choice 2')
		Port2.move(250, 500)
		Port2.resize(200, 100)
		Port2.clicked.connect(self.Port_2_on_click)

		Port3 = QPushButton('Port 3:', self)
		Port3.setToolTip('Answer Choice 3')
		Port3.move(450, 500)
		Port3.resize(200, 100)
		Port3.clicked.connect(self.Port_3_on_click)

		Port4 = QPushButton('Port 4:', self)
		Port4.setToolTip('Answer Choice 4')
		Port4.move(650, 500)
		Port4.resize(200, 100)
		Port4.clicked.connect(self.Port_4_on_click)

		exit = QPushButton('Exit:', self)
		exit.setToolTip('Exit Program')
		exit.move(50, 600)
		exit.resize(200, 100)
		exit.clicked.connect(self.exit_program)

		showCorrectAnswers = QPushButton('Show Correct Answers:', self)
		showCorrectAnswers.setToolTip('Show Correct Answers')
		showCorrectAnswers.move(250, 600)
		showCorrectAnswers.resize(250, 100)
		showCorrectAnswers.clicked.connect(self.showCorrectAnswers)

		showIncorrectAnswers = QPushButton('Show Incorrect Answers:', self)
		showIncorrectAnswers.setToolTip('Show inCorrect Answers')
		showIncorrectAnswers.move(500, 600)
		showIncorrectAnswers.resize(250, 100)
		showIncorrectAnswers.clicked.connect(self.showIncorrectAnswers)

		# Number of Correct Answers Box
		# Width,  then Height
		self.NumberofCorrectAnswers = QLineEdit(self)
		self.NumberofCorrectAnswers.move(900, 100)
		self.NumberofCorrectAnswers.resize(300, 75)
		self.NumberofCorrectAnswers.isReadOnly()

		self.NumberOfCorrectAnswersLabel = QLabel(self)
		self.NumberOfCorrectAnswersLabel.setText("Number of Correct Answers")
		self.NumberOfCorrectAnswersLabel.move(900, 50)

		self.NumberofInCorrectAnswers = QLineEdit(self)
		self.NumberofInCorrectAnswers.move(900, 250)
		self.NumberofInCorrectAnswers.resize(300, 75)
		self.NumberofInCorrectAnswers.isReadOnly()

		self.NumberofInCorrectAnswersLabel = QLabel(self)
		self.NumberofInCorrectAnswersLabel.setText("Number of Incorrect Answers")
		self.NumberofInCorrectAnswersLabel.move(900, 175)
		self.NumberofInCorrectAnswersLabel.resize(300, 75)

		self.Score = QLineEdit(self)
		self.Score.move(900, 400)
		self.Score.resize(300, 75)
		self.Score.isReadOnly()

		self.ScoreLabel = QLabel(self)
		self.ScoreLabel.setText("Current Score")
		self.ScoreLabel.move(900, 350)
		self.Score.resize(300, 75)

		self.DisplayQuestionField = QPlainTextEdit(self)
		self.DisplayQuestionField.move(50, 50)
		self.DisplayQuestionField.resize(800, 425)



		self.show()



	@pyqtSlot()
	def Port_1_on_click(self):
		print('Port 1')

	@pyqtSlot()
	def Port_2_on_click(self):
		print('Port 2')

	@pyqtSlot()
	def Port_3_on_click(self):
		print('Port 3')

	@pyqtSlot()
	def Port_4_on_click(self):
		print('Port 4')

	@pyqtSlot()
	def showCorrectAnswers(self):
		exit()
	@pyqtSlot()
	def showIncorrectAnswers(self):
		exit()
	@pyqtSlot()
	def exit_program(self):
		exit()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = PortQuiz()
	sys.exit(app.exec_())

