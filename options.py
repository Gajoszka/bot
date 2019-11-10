from datetime import *

events = []


def getEvents():
    return events


def addEvent(event):
    events.append(event)


def title():
    name = input("What is the title of the event? ")
    return name


def validTime(date):
    today = datetime.today()
    if today > date:
        return False
    else:
        return True


# def finalDuration(start, end):
# dur = timedelta(start, end)
# y = divmod(dur, 31556926) # seconds in a year
# print("Event lasts " + y)

def dates(check):
    print("What is the start time ?")
    labelsTime = ["Day", "Month", "Year", "Hour", "Minute"]
    startTime = {}
    for el in labelsTime:
        startTime[el] = int(input(el + ": "))
    # s_time = datetime(start_time[2][1], start_time[1][1], start_time[0][1], start_time[3][1], start_time[4][1])
    s_time = datetime(startTime["Year"], startTime["Month"], startTime["Day"], startTime["Hour"], startTime["Minute"])
    #TODO pętla
    if check and validTime(s_time) is False:
        print("This date already passed.")
    return s_time


def validEmail(email):
    if '@' in email:
        if ".com" or ".co.uk" or "ac.uk" or "yahoo.com" or "outlook.com" in email:
            return True
    else:
        return False


def attendees():
    print("How many people do you want to invite?")
    num = int(input())
    attendeesList = []
    for i in range(1, num + 1):
        attendee = input("Please type email address of invited person: ")
        if validEmail(attendee) is False:
            attendee = input("Enter valid email address!")
        else:
            print("")
        attendeesList.append(attendee)
    print(attendeesList)
    return attendees


def description():
    des = input("Describe the event: \n")
    return des


def location():
    loc = input("Where does the event take place? ")
    return loc


def printEvent(summary, start, end, people, description):
    print("Title of the event: " + summary)
    print("Start date: " + str(start))
    print("End date: " + str(end))
    print("Attendees: ", end='')
    print(people)
    print("Description: " + description)
