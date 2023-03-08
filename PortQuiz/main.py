import PortDictInformation
import random

portpoints = 0
guess = -1
shuffledvalues = {}

while guess != 0:

    print("\nPort Quiz")
    print("You'll be given a program and have to guess the port number\n")

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
    shuffledvalues.pop(newvalue4)

    guess = input("Which of the following ports is used by " + portinfo + ":\n"
                  + "Port " + str(newvalue) + "\n"
                  + "Port " + str(newvalue2) + "\n"
                  + "Port " + str(newvalue3) + "\n"
                  + "Port " + str(newvalue4) + "\n"
                  + "Type 0 to exit\n"
                  + "\nWhich port is your guess?\n"
                  + "Answer is: ")

    if guess == 0:
        break
    elif guess == value:
        print("Congratulations, your right!")
        portpoints += 1
        print("Your Current Score: " + str(portpoints))
        print("______________________________________")
        print("______________________________________")

    else:
        print("\nYour choice was not correct.\n"
              "The correct answer is " + value)
        portpoints -= 1
        print("Your Current Score: " + str(portpoints))
        print("______________________________________")
        print("______________________________________")

print("Quiz Over")
print("Total Score: " + str(portpoints))
