"""Definitions of methods that retrieves information provided by the user"""
import logging
from datetime import datetime, timedelta

from calendarApp.menuService import choose_index

LOGGER = logging.getLogger(__name__)


def title():
    name = input("What is the title of the event? ")
    return name


"""checks if start date is before today's date"""


def valid_time(s_date):
    if s_date is None:
        return True
    # gets today's date and adds local timezone to it
    today = datetime.today()
    # today = pytz.utc.localize(today)
    if today > s_date:
        print("This date already past.")
        start_date()
    else:
        return True


"""checks if end date is after start date"""


def check_dates(date1, date2):
    if date2 < date1:
        return False
    else:
        return True


"""takes date and converts it to needed format"""


def input_date(name):
    print("What is the " + name + " time?")
    the_stime = input("Date (default now) format : YYYY-mm-dd HH:mm:ss  or YYYY-mm-dd") or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        the_time = datetime.strptime(the_stime, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        try:
            the_time = datetime.strptime(the_stime, '%Y-%m-%d')
        except ValueError as e:
            # catches exception when format is invalid
            choice = choose_index("Invalid format. Do you want to try again?",
                                  ["Yes", "No"], "Please choose option")
            if choice == 2:
                return None
            else:
                return input_date(name)
    the_time = the_time + timedelta(microseconds=1)
    return the_time


def start_date():
    s_time: datetime = input_date("start")
    if valid_time(s_time) is False:
        print("This date already passed!")
        return start_date()
    return s_time


def end_date(s_time):
    e_time: datetime = input_date("end")
    if check_dates(s_time, e_time) is False:
        print("The end date is before start date!")
        return end_date(s_time)
    return e_time


"""checks if email has '@' and valid domain"""


def valid_email(email):
    if '@' in email:
        if ".com" or ".co.uk" or ".ac.uk" or "yahoo.com" or "outlook.com" in email:
            return True
    else:
        return False


"""checks if number of invites people is integer"""


def attendees():
    attendees_list = []
    print("How many people do you want to invite (default 0)?")
    try:
        num = int(input() or "0")
    except ValueError:
        choice = choose_index("Invalid format. Do you want to try again?",
                              ["Yes", "No"], "Please choose option")
        if choice == 2:
            return None
        else:
            return attendees()
    email_list(num, attendees_list)
    print(attendees_list)
    return attendees_list


"""checks if emails are valid"""


def email_list(num, attendees_list):
    for i in range(1, num + 1):
        attendee = input("Please type email address of invited person: ")
        if valid_email(attendee) is False:
            choice = choose_index("Invalid format. Do you want to try again?",
                                  ["Yes", "No"], "Please choose option")
            if choice == 2:
                return None
            else:
                return email_list(num, attendees_list)
        else:
            attendees_list.append(attendee)
    return attendees_list


def description():
    des = input("Describe the event: \n")
    return des


def event_to_str(event):
    result = None
    try:
        result = "Title of the event: " + event.get("summary", '')
        if event['status'] is not None:
            result += "\nStatus: " + str(event["status"])
        if event.get('start', None) is not None:
            result += "\nStart date: " + str(event['start'].get('dateTime', event['start'].get('date')))
        if event.get('end', None) is not None:
            result += "\nEnd date: " + str(event['end'].get('dateTime', event['end'].get('date', '')))
        # if event['description'] is not None:
        #     result += "\nDescription: " + str(event["description"])
        if event.get('attendees', None) is not None:
            result += "\nAttendees: " + str(event["attendees"])

    except Exception as e:
        LOGGER.error('Failed: ' + str(e))
    return result
