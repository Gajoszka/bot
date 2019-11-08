""" Simple version of getting information """
from datetime import *
#from calendar import create_event
from weather import weatherURL
from actions import title, dates, attendees, description, printEvent, event

listOfEvents = []

def create_event(start, end,  summary, invite, description):
    event = {
        'summary': summary,
        'description': description,
        'start': start,
        'end' : end,
        'attendees': [
            {'email': invite},
        ],
    }
    printEvent(event['summary'], event['start'], event['end'], event['attendees'], event['description'])
    listOfEvents.append(event)

def menu():
    menuOptions = ["1. Add title", "2. Set start and end date", "3. Invite people", "4. Add description", "5. Check weather", "6. Finish and create an event", "7. Exit"]
    for i in menuOptions:
        print(i)
    choice = int(input("Select menu option: "))
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
        if event['start'] == None or event['end'] == None or event['summary'] == None or event['attendees'] == None or event['description'] == None:
            print("You need to fill every menu option!")
            menu()
        else:
            create_event(event['start'], event['end'], event['summary'], event['attendees'], event['description'])
        menu()
    elif choice == 7:
        exit()
    else:
        print("Wrong option. Choose again.")
        menu()


def start():
    print("Hello! Do you want to create an event on your Google Calendar ? ")
    choice = "1. Yes", "2. No, thank you"
    user = int(input(choice))
    if user == 2:
        print("Thank you for your time. See you")
    else:
        print("Great!")
    menu()

start()