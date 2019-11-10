def menuPosition(name, numbers, prompt):
    thisNumber = '1'
    highestNumber = menuDisplay(name, numbers, thisNumber)
    validInput = getValidInput(prompt, thisNumber, highestNumber)
    return validInput

def menuDisplay(name, numbers, thisNumber):
    if len(name) > 0:
        theNumbers = numbers
        setLowestNumber(thisNumber)
        nameDisplay(name)

    index = 0
    for index in range(len(theNumbers)):
        showMenuLine(thisNumber, theNumbers[index])
        thisNumber = chr(ord(thisNumber) + 1)

    lastNumber = chr(ord(thisNumber))
    thisNumber = chr(ord(thisNumber) - 1)

    setHighestNumber(chr(ord(thisNumber) - 1))
    return lastNumber


def nameDisplay(a_name):
    if a_name != '':
        print("\t" + a_name + "\n")

def showMenuLine(label, text):
    print(label + ". " + text)

def setHighestNumber(num):
    highestNum = num

def setLowestNumber(num):
    lowestNum = num

def getValidInput(prompt, lowestNum, highestNum):
    if len(prompt) > 0:
        answer = ''
        invalidAnswer = True
        while invalidAnswer is True:
            userChoice = input(prompt)
            if len(userChoice) > 0:
                answer = userChoice[0]
            else:
                answer = ''
            invalidAnswer = answer < lowestNum or answer > highestNum
    return answer
