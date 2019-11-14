from __future__ import print_function

import json
import logging
import os.path
import pickle

from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
CREDITIONAL_FILE_NAME = 'credentials2.json'
SCOPES_CALENDAR = ['https://www.googleapis.com/auth/calendar']
LOGGER = logging.getLogger(__name__)
calendar = None
credentials = {}


def add_to_calendar(event_body):
    calendar = build('calendar', 'v3', credentials=connect_to_google(SCOPES_CALENDAR))
    json_event = json.loads(event_body.toJson())
    event_to_add = calendar.events().insert(calendarId='primary', body=json_event,
                                            sendNotifications=True).execute()
    try:
        result = calendar.calendarList().list().execute()
    except HttpError as e:
        LOGGER.error('Failed to upload to ftp: ' + str(e))


def get_from_calendar(event_body):
    calendar = build('calendar', 'v3', credentials=connect_to_google(CREDITIONAL_FILE_NAME, SCOPES_CALENDAR))
    try:
        result = calendar.calendarList().list().execute()
    except HttpError as e:
        LOGGER.error('Failed to upload to ftp: ' + str(e))


def connect_to_google(file_name, scopes):
    credential = credentials[scopes]
    if credential is None:
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                credential = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not credential or not credential.valid:
            if credential and credential.expired and credential.refresh_token:
                credential.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(file_name, scopes)
            credential = flow.run_local_server(port=0)
        credentials[scopes] = credential
    return credential
