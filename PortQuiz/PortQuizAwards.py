import self

CorrectAnswersPortDict = {}
IncorrectAnswersPortDict = {}
def CorrectIncorrectResponses(self):
	response = 0

	while response != 0:
		response = input("Do you wish to see the correct or incorrect answers?\n"
						 + "1 for Correct Answers\n"
						 + "2 for Incorrect Answers\n"
						 + "0 for Exit")
		if response == 0:
			final_score()
			break
		if response == 1:
			for CorrectAnswers in CorrectAnswersPortDict:
				print(CorrectAnswers)

		if response == 2:
			for IncorrectAnswers in IncorrectAnswersPortDict:
				print(IncorrectAnswers)


def final_score():
	file_name = self.playername + "Score" + ".txt"

	print("Printing your award certificate: " + file_name)

	awardtext = "Congratulations\n" \
				+ "Name: " + self.playername + "\n" \
				+ "Final Score: " + str(self.portpoints) + "\n"\

	final_score_award = open(file_name, "w")
	final_score_award.write(awardtext)
