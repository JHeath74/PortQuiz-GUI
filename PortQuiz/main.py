import PortDictInformation
import random

portpoints = 0
guess = -1
one = 0
two = 0
three = 0
four = 0
shuffledvalues = {}

while guess != 0:
    guess = 0

    print("\nPort Quiz")
    print("You'll be given a program and have to guess the port number\n")

    portinfo = random.choice(list(PortDictInformation.portDict.values()))

    dictvalue = {i for i in PortDictInformation.portDict if PortDictInformation.portDict[i] == portinfo}

    value = str(dictvalue).replace("{", "").replace("}", "").replace("'", "")
    value2 = random.choice(list(PortDictInformation.portDict.keys()))
    value3 = random.choice(list(PortDictInformation.portDict.keys()))
    value4 = random.choice(list(PortDictInformation.portDict.keys()))

    shuffledvalues = {
        one: value,
        two: value2,
        three: value3,
        four: value4
    }
    if value == value2 or value3 or value4:
        value = random.choice(list(PortDictInformation.portDict.keys()))
    elif value2 == value or value3 or value4:
        value2 = random.choice(list(PortDictInformation.portDict.keys()))
    elif value3 == value or value2 or value4:
        value3 = random.choice(list(PortDictInformation.portDict.keys()))
    elif value4 == value or value2 or value3:
        value4 = random.choice(list(PortDictInformation.portDict.keys()))

    if one == PortDictInformation.portDict.keys():
        shuffledvalues.pop(one)
        one = -1
    elif two == PortDictInformation.portDict.keys():
        shuffledvalues.pop(two)
        two = -1
    elif three == PortDictInformation.portDict.keys():
        shuffledvalues.pop(three)
        three = -1
    elif four == PortDictInformation.portDict.keys():
        shuffledvalues.pop(four)
        four = -1

    guess = input("Which of the following ports is used by " + portinfo + ":\n"
                  + "Port " + str(value) + "\n"
                  + "Port " + str(value2) + "\n"
                  + "Port " + str(value3) + "\n"
                  + "Port " + str(value4) + "\n"
                  + "Type 0 to exit"
                  + "\nWhich port is your guess?\n "
                  + "Answer is: ")

    if guess == value:
        print("Congratulations, your right!")
        portpoints += 1
        print("Your Current Score: " + str(portpoints))
    elif guess == 0:
        break
    else:
        print("\nYour choice was not correct.\n"
              "The correct answer is " + value)
        portpoints -= 1
        print("Your Current Score: " + str(portpoints))

print("Quiz Over")
print("Total Score: " + str(portpoints))
