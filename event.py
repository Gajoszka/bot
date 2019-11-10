"""Code adapted from https://cumoodle.coventry.ac.uk/pluginfile.php/3091515/mod_resource/content/20/Lab%20Activity%20-%20Program%20Modules%20Design%20and%20Development%20%28Menu%29%202019%20v3.pdf"""

def chooseFromMenu(head, options, prompt):
    highestNumber = menuDisplay(head, options)
    validInput = getValidInput(prompt + " (from 1 to " + str(highestNumber) + "): ", highestNumber)
    return int(validInput)


def menuDisplay(head, options):
    if len(head) > 0:
        nameDisplay(head)

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
