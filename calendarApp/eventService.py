"""Code adapted from https://cumoodle.coventry.ac.uk/pluginfile.php/3091515/mod_resource/content/20/Lab%20Activity%20-%20Program%20Modules%20Design%20and%20Development%20%28Menu%29%202019%20v3.pdf"""

from calendarApp.eventData import EventData
from calendarApp.inputService import *
from calendarApp.menuService import chooseOption


class EventService:

    def __init__(self) -> None:
        self.__active = True
        self.__event_data = None
        # creating menu options
        self.__title = "Add title"
        self.__start = "Set start date"
        self.__end = "Set end date"
        self.__attendees = "Invite people"
        self.__description = "Add description"
        self.__cancel = "Exit"

    def run(self):
        self.__event_data = EventData()
        self.__showMenu()
        return self.__event_data

    def __showMenu(self):
        # print the menu while the input from the user is valid
        # (choice was an element of previous menu)
        while self.__active:
            print("----------------------------------------")
            menu = self.__create_menu()
            if len(menu) == 1:
                self.__active = False
            else:
                choice = chooseOption("Menu", menu, "Please choose option")
                self.__runActions(choice)

    """creates menu dynamically based on which options have already been used"""

    def __create_menu(self):
        menu_options = []
        if self.__event_data.summary is None:
            menu_options.append(self.__title)
        if self.__event_data.start is None:
            menu_options.append(self.__start)
        elif self.__event_data.end is None:  # end date can be set only if the start date is set
            menu_options.append(self.__end)
        if self.__event_data.attendees is None:
            menu_options.append(self.__attendees)
        if self.__event_data.description is None:
            menu_options.append(self.__description)
        # static option of menu
        menu_options.append(self.__cancel)
        return menu_options

    """redirects to particular method based on choice made"""

    def __runActions(self, choice):
        if choice == self.__title:
            self.__add_title()
        elif choice == self.__start:
            self.__add_start()
        elif choice == self.__end:
            self.__add_end()
        elif choice == self.__attendees:
            self.__addPeople()
        elif choice == self.__description:
            self.__addDescription()
        else:
            self.__exit()

    """methods that redirects to specific methods and stores information from them as parts of event_data (instance of class EbentData)"""

    def __add_title(self):
        self.__event_data.summary = title()

    def __add_start(self):
        self.__event_data.start = start_date()
        if self.__event_data.start is not None:
            print("Start date: " + self.__event_data.start.strftime('%Y-%m-%d %H:%M:%S'))

    def __add_end(self):
        self.__event_data.end = end_date(self.__event_data.start)
        if self.__event_data.end is not None:
            print("End date: " + self.__event_data.end.strftime('%Y-%m-%d %H:%M:%S'))

    def __addPeople(self):
        self.__event_data.attendees = attendees()

    def __addDescription(self):
        self.__event_data.description = description()

    """make sure user really want to exit creating event"""

    def __exit(self):
        if self.__event_data.check() is False:
            choice = choose_index("You haven't finished creating the event.Do you really want to exit?",
                                  ["Exit anyway", "Go back"], "Please choose option:")
            if choice == 1:
                self.__active = False
                self.__event_data = None
        else:
            self.__active = False
