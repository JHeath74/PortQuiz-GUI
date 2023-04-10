import random
import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QPlainTextEdit, QInputDialog
from PyQt5.QtCore import pyqtSlot, QDir

from PortQuiz import PortQuizAwards, PortDictInformation


class PortQuiz(QWidget):

	def __init__(self):
		super().__init__()

		self.guess = -1
		self.portpoints = 0
		self.correct = 0
		self.incorrect = 0
		self.value = 0
		self.value2 = 0
		self.value3 = 0
		self.value4 = 0
		self.newvalue = 0
		self.newvalue2 = 0
		self.newvalue3 = 0
		self.newvalue4 = 0

		self.DisplayQuestionField = None

		self.Score = QLineEdit(self)
		self.Score.setText("0")

		self.NumberofCorrectAnswers = QLineEdit(self)
		self.NumberofCorrectAnswers.setText("0")

		self.NumberofInCorrectAnswers = QLineEdit(self)
		self.NumberofInCorrectAnswers.setText("0")

		self.ScoreLabel = QLabel(self)
		self.NumberOfCorrectAnswersLabel = QLabel(self)
		self.NumberofInCorrectAnswersLabel = QLabel(self)

		self.title = 'Port Quiz'

		self.setFixedHeight(700)
		self.setFixedWidth(1300)
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)

		port1 = QPushButton("Port 1: %s " % self.newvalue, self)
		port1.setToolTip('Answer Choice 1')
		port1.move(50, 500)
		port1.resize(200, 100)
		port1.clicked.connect(self.Port_1_on_click)

		port2 = QPushButton('Port 2: %d ' % self.newvalue2, self)
		port2.setToolTip('Answer Choice 2')
		port2.move(250, 500)
		port2.resize(200, 100)
		port2.clicked.connect(self.Port_2_on_click)

		port3 = QPushButton('Port 3: %d ' % self.newvalue3, self)
		port3.setToolTip('Answer Choice 3')
		port3.move(450, 500)
		port3.resize(200, 100)
		port3.clicked.connect(self.Port_3_on_click)

		port4 = QPushButton("Port 4: %d" % self.newvalue4, self)
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
		self.PortQuiz()

	def PortQuiz(self):


		shuffledvalues = {}

		playername = QInputDialog().getText(self, "Enter Name",
											"Your name:", QLineEdit.Normal,
											QDir().home().dirName())

		self.DisplayQuestionField.setPlainText('Welcome: ' + str(playername))

		# while guess != 0:

		self.DisplayQuestionField.appendPlainText('				Port Quiz')
		self.DisplayQuestionField.appendPlainText('You''ll be given a protocol'
											' and have to guess the correct'
											' port number by clicking on the'
											' correct button below.')

		portinfo = random.choice(list(PortDictInformation.portDict.values()))
		dictvalue = {i for i in PortDictInformation.portDict if PortDictInformation.portDict[i] == portinfo}

		value = str(dictvalue).replace("{", "").replace("}", "").replace("'", "")
		value2 = random.choice(list(PortDictInformation.portDict.keys()))
		value3 = random.choice(list(PortDictInformation.portDict.keys()))
		value4 = random.choice(list(PortDictInformation.portDict.keys()))

		shuffledvalues[value] = value
		shuffledvalues[value2] = value2
		shuffledvalues[value3] = value3
		shuffledvalues[value4] = value4

		newvalue = random.choice(list(shuffledvalues.keys()))
		shuffledvalues.pop(newvalue)
		newvalue2 = random.choice(list(shuffledvalues.keys()))
		shuffledvalues.pop(newvalue2)
		newvalue3 = random.choice(list(shuffledvalues.keys()))
		shuffledvalues.pop(newvalue3)
		newvalue4 = random.choice(list(shuffledvalues.keys()))

		if newvalue4 is None:
			newvalue4 = random.choice(list(shuffledvalues.keys()))

		shuffledvalues.clear()

		self.refreshButton()

		self.DisplayQuestionField.appendPlainText('')
		self.DisplayQuestionField.appendPlainText("Which of the following ports is used by " + portinfo + ":\n"
												+ "Port: " + str(newvalue) + "\n"
												+ "Port: " + str(newvalue2) + "\n"
												+ "Port: " + str(newvalue3) + "\n"
												+ "Port: " + str(newvalue4) + "\n"
												+ "\nClick the button below with the port "
													"that has your guess?\n")

		print("New Values" + str(newvalue))



	@pyqtSlot()
	def Port_1_on_click(self):
		if self.newvalue == self.value:
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
		if self.newvalue2 == self.value:
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
		if self.newvalue3 == self.value:
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
		if self.newvalue4 == self.value:
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

	def refreshButton(self):
			port1 = QPushButton("Port 1: %d " % self.newvalue, self)
			port2 = QPushButton("Port 2: %d " % self.newvalue2, self)
			port3 = QPushButton("Port 3: %d " % self.newvalue3, self)
			port4 = QPushButton("Port 4: %d " % self.newvalue4, self)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = PortQuiz()
	sys.exit(app.exec_())
