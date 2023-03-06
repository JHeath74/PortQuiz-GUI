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

    one = random.choice(shuffledvalues)

    if one == PortDictInformation.portDict.keys():
        shuffledvalues.pop(one)
    elif two == PortDictInformation.portDict.keys():
        shuffledvalues.pop(two)
    elif three == PortDictInformation.portDict.keys():
        shuffledvalues.pop(three)
    else:
        shuffledvalues.pop(four)

   # two = random.choice(shuffledvalues)
   # three = random.choice(shuffledvalues)
   # four = random.choice(shuffledvalues)

    guess = input("Type What you believe is the correct port or ports for " + portinfo + ":\n"
                  + "One: Port " + str(value) + "\n"
                  + "Two: Port " + str(value2) + "\n"
                  + "Three: Port " + str(value3) + "\n"
                  + "Four: Port " + str(value4) + "\n"
                  + "Type 0 to exit"
                    "\nWhich port is your guess?\n "
                    "Answer is: ")

    if guess == value:
        print("Congratulations, your right!")
        portpoints += 1
    elif guess == 0:
        break
    else:
        print("\nYour choice was not correct.\n"
              "The correct answer is " + value)
        portpoints -= 1

    print("Total Points: " + str(portpoints))
