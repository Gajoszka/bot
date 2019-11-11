"""Code adapted from https://cumoodle.coventry.ac.uk/pluginfile.php/3091515/mod_resource/content/20/Lab%20Activity%20-%20Program%20Modules%20Design%20and%20Development%20%28Menu%29%202019%20v3.pdf"""
from eventData import EventData
from menuService import chooseOption
from inputService import *
from weather import weatherURL


class EventService:
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

        while self.active:
            print("----------------------------------------")
            menu = self._create_menu()
            if len(menu) == 1:
                self.active = False
            else:
                choice = chooseOption("Menu", menu, "Please choose option")
                self._runActions(choice)

    def _create_menu(self):
        _menu_options = []
        if self.event_data.summary is None:
            _menu_options.append(self._title)
        if self.event_data.start is None:
            _menu_options.append(self._start)
        elif self.event_data.end is None:
            _menu_options.append(self._end)
        if self.event_data.attendees is None:
            _menu_options.append(self._attendees)
        if self.event_data.description is None:
            _menu_options.append(self._description)
        _menu_options.append(self._cancel)
        return _menu_options

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

    def _add_title(self):
        self.event_data.summary = title()

    def _add_start(self):
        self.event_data.start = start_date(True)

    def _addDuration(self):
        self.event_data.end = end_date(self.event_data.start, True)

    def _addPeople(self):
        self.event_data.attendees = attendees()

    def _addDescription(self):
        self.event_data.description = description()

    def get_event(self):
        return self.event_data

    def _exit(self):
        if self.event_data.check() is False:
            choice = choose_index("You haven't finished creating the event.Do you really want to exit?",
                                  ["Exit anyway", "Go back"], "Please choose option")
            if choice == 1:
                self.active = False
                self.event_data = None
        else:
            self.active = False
