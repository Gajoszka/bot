from eventData import EventData
from eventServie import EventService
from menuService import chooseOption
from weather import weatherURL


class MenuStart:
    _events = []
    _creation = "Create new event"
    _weather = "Check weather"
    _exit = "Exit"
    active = True
    _menuDefOptions = [_creation, _weather, _exit]

    def showMenu(self):
        while self.active:
            choice = chooseOption("Menu", self._menuDefOptions, "Please choose option ")
            if choice == self._creation:
                self._run_creation()
            elif choice == self._weather:
                self._run_weather()
            elif choice == self._exit:
                self._run_exit()

    def _run_creation(self):
        eventService = EventService()
        eventService.run()
        event_data = eventService.get_event()
        if event_data is not None:
            self._events.append(event_data)
            to_str = EventData()
            to_str.to_string()

    def _run_weather(self):
        weatherURL()

    def _run_exit(self):
        self.active = False
