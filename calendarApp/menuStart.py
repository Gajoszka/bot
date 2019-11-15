"""Display of the main menu and transfers to chosen options to run further parts"""

import logging
from datetime import datetime, timedelta

from calendarApp.calendarService import CalendarService
from calendarApp.eventData import EventData
from calendarApp.eventService import EventService, event_to_str
from calendarApp.menuService import chooseOption
from calendarApp.weather import weatherURL

LOGGER = logging.getLogger(__name__)

class MenuStart:

    def __init__(self) -> None:
        super().__init__()
        self._events = []  # creates empty list of events
        # menu options
        self._creation = "Create new event"
        self._weather = "Check weather"
        self._show_events = "Show events"
        self._exit = "Exit"
        self.active = True
        self.calendarService = CalendarService()
        self.calendarService.calendarId= 'primary'
        self._menuDefOptions = [self._show_events, self._creation, self._weather, self._exit]


    """displays main menu that redirects user to specific options as chosen"""

    def showMenu(self):
        while self.active:
            choice = chooseOption("Menu", self._menuDefOptions, "Please choose option ")
            try:
                if choice == self._creation:
                    self.run_creation()
                elif choice == self._weather:
                    self._run_weather()
                elif choice == self._show_events:
                    self.run_show_events()
                elif choice == self._exit:
                    self._run_exit()
            except Exception as e:
                LOGGER.error('Failed: ' + str(e))

    """prints events that are on user's calendar"""

    def run_show_events(self):
        events_result = self.calendarService.get_from_calendar()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')
        for event in events_result.get('items', []):
            print(event_to_str(event))
            print();

    """redirects user to menu prepared for event creation and then retrieves gained information"""

    def run_creation(self):
        # creating instance of class Event Service
        event_service = EventService()
        event_service.run()
        event_data = event_service.get_event()
        # event_data = self.mock()
        # checks if all essentials data is in event
        # if so, adds event to list and runs method add_to_calendar
        if event_data is not None:
            self.calendarService.add_to_calendar( event_data)
            self._events.append(event_data)
            print(event_data.toStr())
        return event_data

    """redirects to weather file"""

    def _run_weather(self):
        weatherURL()

    """exits program"""

    def _run_exit(self):
        self.active = False

    def mock(self):
        event = EventData()
        event.description = "test2"
        event.end = datetime.today() + timedelta(days=1)
        event.start = datetime.today()
        event.summary = "xlega62@gmail.coma"
        event.attendees = ["ja", "ty"]
        return event
