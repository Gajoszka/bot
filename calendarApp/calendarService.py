"""The part that works along with google calendar API, responsible for logging in, retrieving and adding events"""
from __future__ import print_function

import datetime
import json
import logging
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# logging reports problems and progress
# getLogger creates logger object
LOGGER = logging.getLogger(__name__)


class CalendarService:

    def __init__(self) -> None:
        super().__init__()
        # If modifying these scopes, delete the file token.pickle.
        # gives access to calendar in read/write mode
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.RESOURCE_DIR = './calendarApp/'
        self.CREDENTIAL_FILE_NAME = self.RESOURCE_DIR + 'credentials2.json'
        self.PICKLE_FILE = self.RESOURCE_DIR + 'token.pickle'
        self.credential = None
        self.calendarId = 'primary'

    """adding created event to Google calendar"""

    def add_to_calendar(self, event_body):
        service = build('calendar', 'v3', credentials=self.connect_to_google())
        json_event = json.loads(event_body.toJson())
        try:
            event_to_add = service.events().insert(calendarId=self.calendarId , body=json_event,
                                                   sendNotifications=True).execute()
            result = service.calendarList().list().execute()
        except HttpError as e:
            # logging ERROR - there is a more serious problem which disables software to perform some functions
            LOGGER.error('Failed: ' + str(e))

        """gets events from the calendar and displays them"""

    def get_from_calendar(self):
        service = build('calendar', 'v3', credentials=self.connect_to_google())
        try:
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            return service.events().list(calendarId=self.calendarId , timeMin=now,
                                         maxResults=10, singleEvents=True,
                                         orderBy='startTime').execute()
            # catches error occurred during connecting to https site
            # and displays the error
            # thanks to it program is not ended
        except HttpError as e:
            LOGGER.error('Failed: ' + str(e))
        return None

    """getting credentials for logging to google account"""

    # code adapted from https://developers.google.com/calendar/quickstart/python
    # changes - added if statement for checking occurrence in dictionary
    # no getting and printing events at this point
    def connect_to_google(self):
        # checks if credentials are saved in dictionary
        # if not it follows to create ones
        # if so it gets them from dictionary
        if self.credential is None:
            # If there are no (valid) credentials available, let the user log in.
            self.read_pickle()
        if not self.credential or not self.credential.valid:
            if self.credential and self.credential.expired and self.credential.refresh_token:
                self.credential.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIAL_FILE_NAME, self.SCOPES)
                self.credential = flow.run_local_server(port=0)
                self.save_pickle()
        return self.credential

    def save_pickle(self):
        # Save the credentials for the next run
        with open(self.PICKLE_FILE, 'wb') as token:
            pickle.dump(self.credential, token)

    def read_pickle(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.PICKLE_FILE):
            with open(self.PICKLE_FILE, 'rb') as token:
                self.credential = pickle.load(token)
