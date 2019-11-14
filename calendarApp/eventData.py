import json
from datetime import datetime
# import jsondatetime as j_date
import pytz

from calendarApp.inputService import event_to_str


class EventData:

    def __init__(self) -> None:
        super().__init__()
        # creating empty fields to event
        self.summary = None
        self.description = None
        self.start = None
        self.end = None
        self.attendees = None
        self.endTimeUnspecified = True

    # checks if all required fields are filled
    def check(self):
        return self.start is not None and self.end is not None and self.summary is not None and self.attendees is not None and self.description is not None

    def toStr(self):
        return event_to_str( self.__dict__)


    def toJson(self):
        return json.dumps(self.__dict__, default=event_converter)


def event_converter(o):
    if isinstance(o, datetime):
        # return o.__str__()
        # d = j_date.loads(o)
        return {
            # "date": ,
            "dateTime": pytz.utc.localize(o).isoformat()
            # "timeZone":
        }
