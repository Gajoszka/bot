from options import *
from event import chooseFromMenu
from weather import weatherURL


def showMenu():
    menuDefOptions = ["Add title", "Set start and end date", "Invite people", "Add description", "Check weather",
                      "Finish and create an event", "Exit"]
    menuOptions = menuDefOptions
    run = True
    while run:
        print("----------------------------------------")
        choice = chooseFromMenu("Menu", menuOptions, "Please choose option: ")
        if choice != menuOptions.index("Finish and create an event")+1:
            menuOptions.pop(choice - 1)
        # runActions(choice)


def runActions(choice):
    if choice == 1:
        title()
    elif choice == 2:
        dates()
    elif choice == 3:
        attendees()
    elif choice == 4:
        description()
    elif choice == 5:
        weatherURL()
    elif choice == 6:
        if eventData['start'] == None or eventData['end'] == None or eventData['summary'] == None or eventData[
            'attendees'] == None or \
                eventData['description'] == None:
            print("You need to fill every menu option!")
            showMenu()
        # else:
        #     create_event(eventData['start'], eventData['end'], eventData['summary'], eventData['attendees'],
        #                  eventData['description'])
        showMenu()
    elif choice == 7:
        exit()
    else:
        print("Wrong option. Choose again.")


showMenu()
