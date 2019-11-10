"""Code adapted from https://cumoodle.coventry.ac.uk/pluginfile.php/3091515/mod_resource/content/20/Lab%20Activity%20-%20Program%20Modules%20Design%20and%20Development%20%28Menu%29%202019%20v3.pdf"""
from event import chooseFromMenu
from eventData import EventData
from options import *
from weather import weatherURL

_menuDefOptions = ["Add title", "Set start date", "Duration", "Invite people", "Add description", "Check weather",
                   "Finish and create an event", "Exit"]
_menu_options = _menuDefOptions.copy()


def showMenu():
    run = True
    event_data = EventData()
    while run:
        print("----------------------------------------")
        choice = chooseFromMenu("Menu", _menu_options, "Please choose option")
        choice_def = _menuDefOptions.index(_menu_options[choice])
        if choice != _menu_options.index("Finish and create an event") + 1:
            _menu_options.pop(choice - 1)
        event_data = runActions(choice_def, event_data)


def runActions(choice, event_data):
    if choice == 1:
        event_data.summary = title()
    elif choice == 2:
        event_data.start = dates(True)
    elif choice == 3:
        event_data.end = dates(False)
    elif choice == 4:
        event_data.attendees = attendees()
    elif choice == 5:
        event_data.description = description()
    elif choice == 6:
        weatherURL()
    elif choice == 7:
        if event_data.check() == False:
            print("You need to fill every menu option!")
        else:
            addEvent(event_data)
            # new
            event_data = EventData()
            _menu_options = _menuDefOptions.copy()
    else:
        exit()
    return event_data


showMenu()
