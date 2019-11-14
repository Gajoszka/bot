"""Code adapted from https://cumoodle.coventry.ac.uk/pluginfile.php/3091515/mod_resource/content/20/Lab%20Activity%20-%20Program%20Modules%20Design%20and%20Development%20%28Menu%29%202019%20v3.pdf"""


# returns index from the menu, used when the menu is static and its options does not change position
def choose_index(head, options, prompt):
    highestNumber = menuDisplay(head, options)
    choice = getValidInput(prompt + " (from 1 to " + str(highestNumber) + "): ", highestNumber)
    return int(choice)


# returns option from the menu, used when menu is dynamic and its options change positions
def chooseOption(head, options, prompt):
    highestNumber = menuDisplay(head, options)
    choice = getValidInput(prompt + " (from 1 to " + str(highestNumber) + "): ", highestNumber)
    return options[choice - 1]


# displays the whole menu
def menuDisplay(head, options):
    if len(head) > 0:
        nameDisplay(head)
    index = 0
    for index in range(len(options)):
        showMenuLine(index + 1, options[index])
    return len(options)


# displays menu head formatted, so it is preceded with tab
def nameDisplay(a_name):
    if a_name != '':
        print("\t" + a_name)


# printing menu line with its index at the beginning
def showMenuLine(index, text):
    print(str(index) + ". " + text)


# Getting valid input from the user
def getValidInput(prompt, highestNum):
    invalid_answer = False
    # runs until the invalid_answer - meaning input from the user is valid
    while invalid_answer is False:
        user_choice = input(prompt)
        # checks if user typed anything and if so
        # checks if it is int and takes its first value
        try:
            if len(user_choice) > 0:  # takes first character from user input
                answer = int(user_choice[0])
            else:
                answer = -1
        except ValueError:
            answer = -1
        invalid_answer = answer > 0 and answer <= highestNum

    return answer
