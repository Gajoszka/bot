"""Code adapted from https://cumoodle.coventry.ac.uk/pluginfile.php/3091515/mod_resource/content/20/Lab%20Activity%20-%20Program%20Modules%20Design%20and%20Development%20%28Menu%29%202019%20v3.pdf"""


def choose_index(head, options, prompt):
    highestNumber = menuDisplay(head, options)
    choice = getValidInput(prompt + " (from 1 to " + str(highestNumber) + "): ", highestNumber)
    return int(choice)


def chooseOption(head, options, prompt):
    highestNumber = menuDisplay(head, options)
    choice = getValidInput(prompt + " (from 1 to " + str(highestNumber) + "): ", highestNumber)
    return options[choice - 1]


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


#Getting valid input from the user
def getValidInput(prompt, highestNum):
    invalid_answer = False
    while invalid_answer is False:
        user_choice = input(prompt)
        try:
            if len(user_choice) > 0: # takes first character from user input
                answer = int(user_choice[0])
            else:
                answer = -1
        except ValueError:
            answer = -1
        invalid_answer = answer > 0 and answer <= highestNum

    return answer
