from datetime import datetime

from menuService import choose_index


def title():
    name = input("What is the title of the event? ")
    return name

# checks if start date is before today's date
def valid_time(s_date):
    if s_date is None:
        return True
    today = datetime.today()
    if today > s_date:
        print("This date already past.")
        start_date(True)
    else:
        return True

# checks if end date is after start date
def check_dates(date1, date2):
    if date2 < date1:
        return False
    else:
        return True

# takes date and converts it to needed format
def input_date(name):
    print("What is the " + name + " time?")
    try:
        the_time = datetime.strptime(input("Date (YYYY-mm-dd HH:mm:ss): "), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        # catches exception when format is invalid
        choice = choose_index("Invalid format. Do you want to try again?",
                              ["Yes", "No"], "Please choose option")
        if choice == 2:
            return None
        else:
            input_date(name)
    return the_time


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
        end_date(s_time, True)
    return e_time

# checks if email has '@' and valid domain
def valid_email(email):
    if '@' in email:
        if ".com" or ".co.uk" or ".ac.uk" or "yahoo.com" or "outlook.com" in email:
            return True
    else:
        return False

# checks if number of invites people is integer
def attendees():
    attendees_list = []
    print("How many people do you want to invite?")
    try:
        num = int(input())
    except ValueError:
        choice = choose_index("Invalid format. Do you want to try again?",
                                ["Yes", "No"], "Please choose option")
        if choice == 2:
            return None
        else:
            attendees()
    email_list(num, attendees_list)
    print(attendees_list)
    return attendees_list

# checks if emails are valid
def email_list(num, attendees_list):
    for i in range(1, num + 1):
        attendee = input("Please type email address of invited person: ")
        if valid_email(attendee) is False:
            choice = choose_index("Invalid format. Do you want to try again?",
                                    ["Yes", "No"], "Please choose option")
            if choice == 2:
                return None
            else:
                email_list(num, attendees_list)
        else:
            attendees_list.append(attendee)
    return attendees_list

def description():
    des = input("Describe the event: \n")
    return des
