from options import *
from event import menuPosition
from weather import weatherURL

def showMenu(events):
    menuOptions = ["Add title", "Set start and end date", "Invite people", "Add description", "Check weather", "Finish and create an event", "Exit"]
    run = True
    while run:
        print("----------------------------------------")
        choice = menuPosition("Menu", menuOptions, "Please choose option: ")

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
        if event['start'] == None or event['end'] == None or event['summary'] == None or event['attendees'] == None or \
                event['description'] == None:
            print("You need to fill every menu option!")
            showMenu()
        else:
            create_event(event['start'], event['end'], event['summary'], event['attendees'], event['description'])
        showMenu()
    elif choice == 7:
        exit()
    else:
        print("Wrong option. Choose again.")
        showMenu()