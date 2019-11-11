from menuService import chooseOption
from eventServie import EventService
from eventData import EventData


class MenuStart:
    _events = []
    _creation = "Create new event"
    _exit = "Exit"
    active = True
    _menuDefOptions = [_creation, _exit]
    def showMenu(self):
        while self.active:
            choice = chooseOption("Menu", self._menuDefOptions, "Please choose option ")
            if choice == self._creation:
                self._runCreation()
            elif choice == self._exit:
                self._runExit()

    def _runCreation(self):
        eventService = EventService()
        eventService.run()
        eventData = eventService.get_event()
        if eventData != None:
            self._events.append(eventData)
            to_str = EventData
            to_str.to_string()

    def _runExit(self):
        self.active = False

