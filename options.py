from datetime import *

events = []

eventData = {
    'summary': None,
    'description': None,
    'start': None,
    'end': None,
    'attendees': [
        {'email': None},
    ],
}


def getEvents():
    return events


def uploadEventList(theList):
    events = theList


def title():
    name = input("What is the title of the event? ")
    eventData['summary'] = name
    return name


def validTime(start):
    today = datetime.today()
    if today > start:
        return False
    else:
        return True


# def finalDuration(start, end):
# dur = timedelta(start, end)
# y = divmod(dur, 31556926) # seconds in a year
# print("Event lasts " + y)

def dates():
    print("What is the start time ?")
    labelsTime = ["Day", "Month", "Year", "Hour", "Minute"]
    startTime = {}
    for el in labelsTime:
        startTime[el] = int(input(el + ": "))
    # s_time = datetime(start_time[2][1], start_time[1][1], start_time[0][1], start_time[3][1], start_time[4][1])
    s_time = datetime(startTime["Year"], startTime["Month"], startTime["Day"], startTime["Hour"], startTime["Minute"])

    print("What is the end time ?")
    endTime = {}
    for el in labelsTime:
        endTime[el] = int(input(el + ": "))
    # e_time = datetime(end_time[2][1], end_time[1][1], end_time[0][1], end_time[3][1], end_time[4][1])
    e_time = datetime(endTime["Year"], endTime["Month"], endTime["Day"], endTime["Hour"], endTime["Minute"])

    if validTime(s_time) is False:
        print("This date already passed.")
        dates()
    elif e_time < s_time:  # checking if end date is after start date
        print("The end date is before the start date! Put information again")
        dates()
    else:
        message = "The start date is" + str(s_time) + ". The end date is" + str(e_time) + "."
        print(message)
        eventData['start'] = s_time
        eventData['end'] = e_time
    return s_time, e_time, message


def validEmail(email):
    if '@' in email:
        if ".com" or ".co.uk" in email:
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
    eventData['attendees'] = attendees
    return attendees


def description():
    des = input("Describe the event: \n")
    eventData['description'] = des
    return des


def location():
    loc = input("Where does the event take place? ")
    eventData['location'] = loc
    return loc


def printEvent(summary, start, end, people, description):
    print("Title of the event: " + summary)
    print("Start date: " + str(start))
    print("End date: " + str(end))
    print("Attendees: ", end='')
    print(people)
    print("Description: " + description)

