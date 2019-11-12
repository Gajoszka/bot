# from calendarAPI import service
from eventData import EventData
from eventService import EventService
from menuService import chooseOption
from weather import weatherURL
from quickCalendar2 import add_to_calendar


class MenuStart:
    _events = [] # creates empty list of events
    # menu options
    _creation = "Create new event"
    _weather = "Check weather"
    _exit = "Exit"
    active = True
    _menuDefOptions = [_creation, _weather, _exit]

    def showMenu(self):
        while self.active:
            choice = chooseOption("Menu", self._menuDefOptions, "Please choose option ")
            if choice == self._creation:
                self.run_creation()
            elif choice == self._weather:
                self._run_weather()
            elif choice == self._exit:
                self._run_exit()

    def run_creation(self):
        # creating instance of class Event Service
        event_service = EventService()
        event_service.run()
        event_data = event_service.get_event()
        # checks if all essentials data is in event
        # if so, adds event to list
        if event_data is not None:
            self._events.append(event_data)
            event_data.printing()
            return event_data
            #event_to_add = service.events().insert(calendarId='primary', body=event_data).execute()

    def _run_weather(self):
        weatherURL()

    # exits program
    def _run_exit(self):
        self.active = False
