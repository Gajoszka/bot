from datetime import datetime,timedelta
from eventData import EventData
from updateCalendary import add_to_calendar

event = EventData()
event.description = "test"
event.end = datetime.today() + timedelta(days=1)
event.start = datetime.today()
print(event.toJson())
add_to_calendar(event)
