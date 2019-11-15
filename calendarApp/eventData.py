import json
from datetime import datetime

# import jsondatetime as j_date
import pytz


class EventData:

    def __init__(self) -> None:
        super().__init__()
        # creating empty fields to event
        self.summary = None
        self.description = None
        self.start: datetime = None
        self.end: datetime = None
        self.attendees = None
        self.endTimeUnspecified = True

    """checks if all required fields are filled"""

    def check(self):
        return self.start is not None and self.end is not None and self.summary is not None and self.attendees is not None and self.description is not None

    """creates dictionary from received data"""

    def toStr(self):
        dictionary = self.__dict__
        return "Title of the event: " + dictionary.get("summary", '') + "\n Start date: " + str(
            dictionary.get("start", None)) + "\n End date: " + str(
            dictionary.get("end", None)) + "\n Attendees: " + str(
            dictionary.get("attendees", [])) + "\n Description: " + dictionary.get("description")

    """makes dictionary JSON serialized"""

    def toJson(self):
        return json.dumps(self.__dict__, default=event_converter)


def event_converter(o):
    if isinstance(o, datetime):
        # return o.__str__()
        # d = j_date.loads(o)
        return {
            # dds local timezone to dates
            # "date": ,
            "dateTime": pytz.utc.localize(o).isoformat()
            # "timeZone":
        }
