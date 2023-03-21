import random

import self as self


class main:

	def __init__(self):
		self.guess = 1
		self.portpoints = 0
		self.correct = 0
		self.incorrect = 0
		self.newvalue = 0
		self.newvalue2 = 0
		self.newvalue3 = 0
		self.newvalue4 = 0

		self.playername = " "

		self.shuffledvalues = {}




	playername = input("Please Enter your name and press the enter key: ")

	while guess != 0:

		print("\nPort Quiz")
		print("You'll be given a program and have to guess the port number\n")

		portinfo = random.choice(list(self.PortDictInformation.portDict.values()))
		dictvalue = {i for i in self.PortDictInformation.portDict if self.PortDictInformation.portDict[i] == portinfo}

		value = str(dictvalue).replace("{", "").replace("}", "").replace("'", "")
		value2 = random.choice(list(self.PortDictInformation.portDict.keys()))
		value3 = random.choice(list(self.PortDictInformation.portDict.keys()))
		value4 = random.choice(list(self.PortDictInformation.portDict.keys()))

		self.shuffledvalues[value] = value
		self.shuffledvalues[value2] = value2
		self.shuffledvalues[value3] = value3
		self.shuffledvalues[value4] = value4

		newvalue = random.choice(list(self.shuffledvalues.keys()))
		self.shuffledvalues.pop(newvalue)
		newvalue2 = random.choice(list(self.shuffledvalues.keys()))
		self.shuffledvalues.pop(newvalue2)
		newvalue3 = random.choice(list(self.shuffledvalues.keys()))
		self.shuffledvalues.pop(newvalue3)
		newvalue4 = random.choice(list(self.shuffledvalues.keys()))
		self.shuffledvalues.clear()

		guess = input("Which of the following ports is used by " + portinfo + ":\n"
					  + "Port: " + str(newvalue) + "\n"
					  + "Port: " + str(newvalue2) + "\n"
					  + "Port: " + str(newvalue3) + "\n"
					  + "Port: " + str(newvalue4) + "\n"
					  + "Type 0 to exit\n"
					  + "\nWhich port is your guess?\n"
					  + "Answer is: ")

		if guess == "0":
			self.PortQuizAwards.CorrectIncorrectResponses(playername)
		# break

		elif guess == value:
			print("Congratulations, your right!")
			self.portpoints += 1
			self.correct += 1
			print("Your Current Score: " + str(self.portpoints))
			self.PortQuizAwards.CorrectAnswersPortDict["guess"] = "portinfo"
			self.shuffledvalues.clear()
			print("______________________________________")
			print("______________________________________")

		else:
			print("\nYour choice was not correct.\n"
				  "The correct answer is " + value)
			self.portpoints -= 1
			self.incorrect += 1
			self.PortQuizAwards.IncorrectAnswersPortDict["guess"] = "portinfo"
			self.shuffledvalues.clear()
			print("Your Current Score: " + str(self.portpoints))
			print("______________________________________")
			print("______________________________________")

		print("Quiz Over")
		print("Total Score: " + str(self.portpoints))
		print("Number of correct guesses: " + str(self.correct))
		print("Number of incorrect guesses: " + str(self.incorrect))
