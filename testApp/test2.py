import logging
from datetime import datetime, timedelta

from calendarApp.eventData import EventData
from testApp.updateCalendary import add_to_calendar

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
event = EventData()
event.description = "test2"
event.end = datetime.today() + timedelta(days=1)
event.start = datetime.today()
event.summary = "xlega62@gmail.coma"
event.attendees = ["ja", "ty"]
LOGGER.info(event.toJson())
add_to_calendar(event)
