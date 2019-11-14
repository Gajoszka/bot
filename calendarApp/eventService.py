"""displays menu to create an event and stores information as an instance of EventData"""
import json

from calendarApp.eventData import EventData
from calendarApp.menuService import chooseOption, choose_index
from calendarApp.inputService import *


class EventService:
    # creating menu options
    _title = "Add title"
    _start = "Set start date"
    _end = "Set end date"
    _attendees = "Invite people"
    _description = "Add description"
    _cancel = "Exit"

    def __init__(self) -> None:
        self.active = True
        self.event_data = EventData()

    def run(self):
        self.showMenu()


    def showMenu(self):
        # print the menu while the input from the user is valid
        # (choice was an element of previous menu)
        while self.active:
            print("----------------------------------------")
            menu = self._create_menu()
            if len(menu) == 1:
                self.active = False
            else:
                choice = chooseOption("Menu", menu, "Please choose option")
                self._runActions(choice)

    """creates menu dynamically based on which options have already been used"""
    def _create_menu(self):
        _menu_options = []
        if self.event_data.summary is None:
            _menu_options.append(self._title)
        if self.event_data.start is None:
            _menu_options.append(self._start)
        elif self.event_data.end is None:  # end date can be set only if the start date is set
            _menu_options.append(self._end)
        if self.event_data.attendees is None:
            _menu_options.append(self._attendees)
        if self.event_data.description is None:
            _menu_options.append(self._description)
        # static option of menu
        _menu_options.append(self._cancel)
        return _menu_options

    """redirects to particular method based on choice made"""
    def _runActions(self, choice):
        if choice == self._title:
            self._add_title()
        elif choice == self._start:
            self._add_start()
        elif choice == self._end:
            self._addDuration()
        elif choice == self._attendees:
            self._addPeople()
        elif choice == self._description:
            self._addDescription()
        else:
            self._exit()

    """methods that redirects to specific methods and stores information from them as parts of event_data (instance of class EbentData)"""
    def _add_title(self):
        self.event_data.summary = title()

    def _add_start(self):
        self.event_data.start = start_date(True)

    def _addDuration(self):
        self.event_data.end = end_date(self.event_data.start, True)
        # make start and end date JSON serialized
        self.event_data.start = json.dumps(self.event_data.start, indent=4, sort_keys=True, default=str)
        self.event_data.end = json.dumps(self.event_data.end, indent=4, sort_keys=True, default=str)

    def _addPeople(self):
        self.event_data.attendees = attendees()

    def _addDescription(self):
        self.event_data.description = description()

    def get_event(self):
        return self.event_data

    """make sure user really want to exit creating event"""
    def _exit(self):
        if self.event_data.check() is False:
            choice = choose_index("You haven't finished creating the event.Do you really want to exit?",
                                  ["Exit anyway", "Go back"], "Please choose option")
            # clears event_data to be empty
            if choice == 1:
                self.active = False
                self.event_data = None
        # goes back to creation menu
        else:
            self.active = False
