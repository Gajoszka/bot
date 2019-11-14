from __future__ import print_function

import json
import logging
import os.path
import pickle
import datetime

from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
RESOURCE_DIR = './calendarApp/'
CREDENTIAL_FILE_NAME = RESOURCE_DIR + 'credentials2.json'
PICKLE_FILE = RESOURCE_DIR + 'token.pickle'
SCOPE_CALENDAR = 'https://www.googleapis.com/auth/calendar'
LOGGER = logging.getLogger(__name__)
calendar = None
credentialsDic: dict = {}


def add_to_calendar(event_body):
    calendar = build('calendar', 'v3', credentials=connect_to_google(SCOPE_CALENDAR))
    json_event = json.loads(event_body.toJson())
    event_to_add = calendar.events().insert(calendarId='primary', body=json_event,
                                            sendNotifications=True).execute()
    try:
        result = calendar.calendarList().list().execute()
    except HttpError as e:
        LOGGER.error('Failed: ' + str(e))


def get_from_calendar():
    calendar = build('calendar', 'v3', credentials=connect_to_google(CREDENTIAL_FILE_NAME, SCOPE_CALENDAR))
    try:
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        return calendar.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
    except HttpError as e:
        LOGGER.error('Failed: ' + str(e))
    return None


def connect_to_google(file_name, scope):
    if scope not in credentialsDic:
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        credential = None
        if os.path.exists(PICKLE_FILE):
            with open(PICKLE_FILE, 'rb') as token:
                credential = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not credential or not credential.valid:
            if credential and credential.expired and credential.refresh_token:
                credential.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(file_name, [scope])
                credential = flow.run_local_server(port=0)
                credentialsDic[scope] = credential
                # Save the credentials for the next run
                with open(PICKLE_FILE, 'wb') as token:
                    pickle.dump(credential, token)
    else:
        credential = credentialsDic[scope]
    return credential
