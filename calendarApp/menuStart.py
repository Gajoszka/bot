import logging

from calendarApp.eventService import EventService
from calendarApp.menuService import chooseOption
from calendarApp.weather import weatherURL
from calendarApp.calendarService import add_to_calendar, get_from_calendar
from calendarApp.inputService import event_to_str

LOGGER = logging.getLogger(__name__)


class MenuStart:
    _events = []  # creates empty list of events
    # menu options
    _creation = "Create new event"
    _weather = "Check weather"
    _show_events = "Show events"
    _exit = "Exit"
    active = True
    _menuDefOptions = [_show_events, _creation, _weather, _exit]

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

    def run_show_events(self):
        events_result = get_from_calendar()
        # for event in events_result.get('items', []):
        #     event_to_str(event)

    def run_creation(self):
        # creating instance of class Event Service
        event_service = EventService()
        event_service.run()
        event_data = event_service.get_event()
        # checks if all essentials data is in event
        # if so, adds event to list
        if event_data is not None:
            add_to_calendar(event_service.get_event())
            self._events.append(event_data)
            print(event_data.toStr())
            # a = event_data.toJson(event_data)
            # add_to_calendar(a)
            return event_data

    def _run_weather(self):
        weatherURL()

    # exits program
    def _run_exit(self):
        self.active = False
