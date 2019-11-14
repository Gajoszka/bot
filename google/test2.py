from datetime import datetime, timedelta

from calendarApp.eventData import EventData
from calendarApp.updateCalendary import add_to_calendar

event = EventData()
event.description = "test2"
event.end = datetime.today() + timedelta(days=1)
event.start = datetime.today()
event.summary = "xlega62@gmail.coma"
event.attendees = ["ja", "ty"]
print(event.toJson())
add_to_calendar(event)
