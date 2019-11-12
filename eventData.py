class EventData:

    def __init__(self) -> None:
        super().__init__()
        # creating empty fields to event
        self.summary = None
        self.description = None
        self.start = None
        self.end = None
        self.attendees = None

    # checks if all required fields are filled
    def check(self):
        return self.start is not None and self.end is not None and self.summary is not None and self.attendees is not None and self.description is not None

    # prints summary of the event
    def printing(self):
        print("Title of the event: " + self.summary
              + "\n Start date: " + str(self.start)
              + "\n Duration: " + str(self.end)
              + "\n Attendees: " + str(self.attendees)
              + "\n Description: " + self.description)