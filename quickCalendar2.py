"""Code adapted from https://github.com/gsuitedevs/python-samples/blob/master/calendar/quickstart/quickstart.py"""
from __future__ import print_function

import json

from eventService import EventService
from eventData import EventData

import datetime
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def add_to_calendar(event_body):
    # part copied from the URL presented at the top
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials2.json', SCOPES)
            creds = flow.run_local_server(port=0)
    # deleted the part that saves the credentials, so each new user
    # can login to their own account

    # deleted the part that retrieves events from calendar
    # instead created the code that adds new event

    service = build('calendar', 'v3', credentials=creds)
    get_new_event = EventService()
    # event_details = EventData()
    event_to_add = service.events().insert(calendarId='primary', body=(event_body.toJson()))
