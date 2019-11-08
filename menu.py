from actions import *
from weather import weatherURL

def addTitle():
    title()

def setDates():
    dates()

def addPeople():
    attendees()

def addDescription():
    description()

def checkWeather():
    weatherURL()

def menu(i):
    menuOptions = {
        1: "Add title",
        2: "Set start and end date",
        3: "Invite people",
        4: "Add description",
        5: "Check weather",
        6: "Finish and create an event",
        7.: "Exit"
    }

