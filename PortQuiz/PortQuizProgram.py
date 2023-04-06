import random

from PortQuiz import PortDictInformation, PortQuizAwards

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QInputDialog, QLineEdit


class PortQuizProgram:

	def __int__(self):
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

		self.DisplayQuestionField.appendPlainText('')
		self.DisplayQuestionField.appendPlainText("Which of the following ports is used by " + portinfo + ":\n"
												+ "Port: " + str(newvalue) + "\n"
												+ "Port: " + str(newvalue2) + "\n"
												+ "Port: " + str(newvalue3) + "\n"
												+ "Port: " + str(newvalue4) + "\n"
												+ "\nClick the button below with the port "
													"that has your guess?\n")
