class EventData:

    def __init__(self) -> None:
        super().__init__()
        self.summary= None
        self.description = None
        self.start = None
        self.end = None
        self.attendees = None

    def check(self):
        return self.start is not None and self.end is not None and self.summary is not None and self.attendees is not None and self.description is not None

    def to_string(self):
        print("Title of the event: " + str(self.summary)
        + "\n Start date: " + str(self.start)
        + "\n Duration: " + str(self.end)
        + "\n Attendees: " + self.attendees
        +"\n Description: " + str(self.description))