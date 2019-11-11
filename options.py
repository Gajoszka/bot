from datetime import *
from datetime import datetime


def title():
    name = input("What is the title of the event? ")
    return name


def valid_time(s_date):
    today = datetime.today()
    if today > s_date:
        print("This date already past.")
        start_date(True)
    else:
        return True


def check_dates(date1, date2):
    if date2 - date1 < 0:
        return False
    else:
        return True


def input_date(name):
    print("What is the " + name + " time?")
    labels_time = ["Day", "Month", "Year", "Hour", "Minute"]
    date = {}
    for el in labels_time:
        date[el] = int(input(el + ": "))
    # DATE = datetime(start_time[2][1], start_time[1][1], start_time[0][1], start_time[3][1], start_time[4][1])
    s_time = datetime(date["Year"], date["Month"], date["Day"], date["Hour"],
                     date["Minute"])
    return s_time


def start_date(check):
    s_time: datetime = input_date("start")
    if check and valid_time(s_time) is False:
        print("This date already passed!")
        start_date(True)
    return s_time


def end_date(s_time, check):
    e_time: datetime = input_date("end")
    if check and check_dates(s_time, e_time) is False:
        print("The end date is before start date!")
        end_date(True)
    return e_time


def valid_email(email):
    if '@' in email:
        if ".com" or ".co.uk" or "ac.uk" or "yahoo.com" or "outlook.com" in email:
            return True
    else:
        return False


def attendees():
    print("How many people do you want to invite?")
    num = int(input())
    attendees_list = []
    for i in range(1, num + 1):
        attendee = input("Please type email address of invited person: ")
        if valid_email(attendee) is False:
            attendee = input("Enter valid email address!")
        else:
            print("")
        attendees_list.append(attendee)
    print(attendees_list)
    return attendees


def description():
    des = input("Describe the event: \n")
    return des


def printEvent(summary, start, end, people, description):
    print("Title of the event: " + summary)
    print("Start date: " + str(start))
    print("End date: " + str(end))
    print("Attendees: ", end='')
    print(people)
    print("Description: " + description)
