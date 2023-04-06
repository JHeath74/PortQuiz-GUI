import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QPlainTextEdit
from PyQt5.QtCore import pyqtSlot

from PortQuiz import PortQuizAwards
from PortQuiz.PortQuizProgram import PortQuizProgram


class PortQuiz(QWidget):

	def __init__(self):
		super().__init__()

		self.DisplayQuestionField = None

		self.Score = QLineEdit(self)
		self.Score.setText("0")

		self.NumberofCorrectAnswers = QLineEdit(self)
		self.NumberofCorrectAnswers.setText("0")

		self.NumberofInCorrectAnswers = QLineEdit(self)
		self.NumberofInCorrectAnswers.setText("0")

		self.NumberofInCorrectAnswersLabel = QLabel(self)
		self.ScoreLabel = QLabel(self)
		self.NumberOfCorrectAnswersLabel = QLabel(self)

		self.title = 'Port Quiz'

		self.setFixedHeight(700)
		self.setFixedWidth(1300)
		self.initUI()

		PortQuizProgram.PortQuiz(self)

	def initUI(self):
		self.setWindowTitle(self.title)

		port1 = QPushButton("Port 1: ", self)
		port1.setToolTip('Answer Choice 1')
		port1.move(50, 500)
		port1.resize(200, 100)
		port1.clicked.connect(self.Port_1_on_click)

		port2 = QPushButton('Port 2: ', self)
		port2.setToolTip('Answer Choice 2')
		port2.move(250, 500)
		port2.resize(200, 100)
		port2.clicked.connect(self.Port_2_on_click)

		port3 = QPushButton('Port 3: ', self)
		port3.setToolTip('Answer Choice 3')
		port3.move(450, 500)
		port3.resize(200, 100)
		port3.clicked.connect(self.Port_3_on_click)

		port4 = QPushButton('Port 4: ', self)
		port4.setToolTip('Answer Choice 4')
		port4.move(650, 500)
		port4.resize(200, 100)
		port4.clicked.connect(self.Port_4_on_click)

		exitprogram = QPushButton('Exit:', self)
		exitprogram.setToolTip('Exit Program')
		exitprogram.move(50, 600)
		exitprogram.resize(200, 100)
		exitprogram.clicked.connect(self.exit_program)

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

		self.NumberofCorrectAnswers.move(900, 100)
		self.NumberofCorrectAnswers.resize(300, 75)
		self.NumberofCorrectAnswers.isReadOnly()

		self.NumberOfCorrectAnswersLabel.setText("Number of Correct Answers")
		self.NumberOfCorrectAnswersLabel.move(900, 50)

		self.NumberofInCorrectAnswers.move(900, 250)
		self.NumberofInCorrectAnswers.resize(300, 75)
		self.NumberofInCorrectAnswers.isReadOnly()

		self.NumberofInCorrectAnswersLabel.setText("Number of Incorrect Answers")
		self.NumberofInCorrectAnswersLabel.move(900, 175)
		self.NumberofInCorrectAnswersLabel.resize(300, 75)

		self.ScoreLabel.setText("Current Score")
		self.ScoreLabel.move(900, 350)

		self.Score.move(900, 400)
		self.Score.resize(300, 75)
		self.Score.isReadOnly()

		self.DisplayQuestionField = QPlainTextEdit(self)
		self.DisplayQuestionField.move(50, 50)
		self.DisplayQuestionField.resize(800, 425)

		self.show()

	@pyqtSlot()
	def Port_1_on_click(self):
		if self.guess == self.value:
			self.portpoints += 1
			self.correct += 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo
		else:
			self.portpoints -= 1
			self.correct -= 1
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo

	@pyqtSlot()
	def Port_2_on_click(self):
		if self.guess == self.value:
			self.portpoints += 1
			self.correct += 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo
		else:
			self.portpoints -= 1
			self.correct -= 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo

	@pyqtSlot()
	def Port_3_on_click(self):
		if self.guess == self.value:
			self.portpoints += 1
			self.correct += 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo
		else:
			self.portpoints -= 1
			self.correct -= 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo

	@pyqtSlot()
	def Port_4_on_click(self):
		if self.guess == self.value:
			self.portpoints += 1
			self.correct += 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo
		else:
			self.portpoints -= 1
			self.correct -= 1
			self.Score.setText(self.portpoints)
			self.NumberofCorrectAnswers.setText(self.correct)
			PortQuizAwards.CorrectAnswersPortDict[self.guess] = self.portinfo

	@pyqtSlot()
	def showCorrectAnswers(self):
		PortQuizAwards.CorrectAnswersPortDict.items()
		for key, value in PortQuizAwards.CorrectAnswersPortDict.items():
			self.DisplayQuestionField.setPlainText("Port: {} - Portocol: {}\n".format(key, value))

	@pyqtSlot()
	def showIncorrectAnswers(self):
		for key, value in PortQuizAwards.IncorrectAnswersPortDict.items():
			self.DisplayQuestionField.setPlainText("Port: {} - Portocol: {}\n".format(key, value))

	@pyqtSlot()
	def exit_program(self):
		exit()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = PortQuiz()
	sys.exit(app.exec_())
