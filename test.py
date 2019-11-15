import calendarApp.config as config
from calendarApp.menuStart import MenuStart

name = input("Hello introduce yourself: ")
config.init("config.yaml")

if name is not None:
    config.add_setting("name",name)
menu_start = MenuStart()
menu_start.run()
