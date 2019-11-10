class EventData:
    summary: None
    description: None
    start: None
    end: None
    attendees: [
        {'email': None},
    ]

    def check(self):
        return self.start != None and self.end != None and self.summary != None and self.attendees != None and self.description != None
