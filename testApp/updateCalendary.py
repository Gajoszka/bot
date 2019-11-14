from __future__ import print_function
import logging
import json

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
from googleapiclient.errors import HttpError

SCOPES_CALENDAR = ['https://www.googleapis.com/auth/calendar']

SCOPES_EVENT = ['https://www.googleapis.com/auth/calendar.events']


# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         # with open('token.pickle', 'wb') as token:
#         #     pickle.dump(creds, token)
#
#     service = build('calendar', 'v3', credentials=creds)
#
#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#     print('Getting the upcoming 10 events')
#     events_result = service.events().list(calendarId='primary', timeMin=now,
#                                           maxResults=10, singleEvents=True,
#                                           orderBy='startTime').execute()
#     events = events_result.get('items', [])
#
#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])

def add_to_calendar(event_body):
    calendar = build('calendar', 'v3', credentials=connect_to_goole(SCOPES_CALENDAR))
    result = calendar.events().list(calendarId='xlega62@gmail.com').execute()
    json_event = json.loads(event_body.toJson())
    try:
        event_to_add = calendar.events().insert(calendarId='xlega62@gmail.com', body=json_event,
                                                sendNotifications=True).execute()
    except HttpError as e:
        logging.error('Failed to upload to ftp: ' + str(e))
    result = calendar.calendarList().list().execute()


def connect_to_goole(scopes):
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
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        # with open('token.pickle', 'wb') as token:
        #     pickle.dump(creds, token)
    return creds
