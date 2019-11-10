def chooseFromMenu(name, options, prompt):
    highestNumber = menuDisplay(name, options)
    validInput = getValidInput(prompt + " (from 1 to " + str(highestNumber) + ")", highestNumber)
    return int(validInput)


def menuDisplay(name, options):
    if len(name) > 0:
        nameDisplay(name)

    index = 0
    for index in range(len(options)):
        showMenuLine(index + 1, options[index])

    return len(options)


def nameDisplay(a_name):
    if a_name != '':
        print("\t" + a_name + "\n")


def showMenuLine(index, text):
    print(str(index) + ". " + text)


def getValidInput(prompt, highestNum):
    invalidAnswer = False
    while invalidAnswer is False:
        userChoice = input(prompt)
        try:
            if len(userChoice) > 0:
                answer = int(userChoice[0])
            else:
                answer = -1
        except ValueError:
            answer = -1
        invalidAnswer = answer > 0 and answer <= highestNum

    return answer
