import random

from PortQuiz import PortDictInformation, PortQuizAwards

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QInputDialog, QLineEdit



class PortQuizProgram:

	def PortQuiz(self):
		guess = -1
		portpoints = 0
		correct = 0
		incorrect = 0
		newvalue = 0
		newvalue2 = 0
		newvalue3 = 0
		newvalue4 = 0

		shuffledvalues = {}

		playername = QInputDialog().getText(self, "Enter Name",
												 "Your name:", QLineEdit.Normal,
												 QDir().home().dirName())

		self.DisplayQuestionField.setPlainText('Welcome: ' + str(playername))

		#while guess != 0:

		self.DisplayQuestionField.appendPlainText('')
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
					  + "\nWhich port is your guess?\n"
					  + "Answer is: ")



