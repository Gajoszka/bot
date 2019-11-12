# """Code adapted from https://www.dropbox.com/s/21fabn7cct2cjts/Calendar_Create_Event_Functionv.py?dl=0"""
# import pickle
# import pprint
#
# from google_auth_oauthlib.flow import Flow  # using Flow function instead of InstalledAppsFLow
# from googleapiclient.discovery import build
#
# flow = Flow.from_client_secrets_file("google/credentials.json",
#                                      scopes='https://www.googleapis.com/auth/calendar')  # access to calendar in mode read/write
# credentials = flow.run_console()
#
# pickle.dump(credentials, open("token.pkl", "wb"))
# credentials = pickle.load(open("token.pkl", "rb"))
# service = build("calendar", "v3", credentials=credentials)
#
# result = service.calendarList().list().execute()
# calendar_id = result['items'][0]['id']
#
# pp = pprint.PrettyPrinter(indent=4)  # use pprint for nicer view
# timezone = 'Australia/Sydney'  # enter your timezone
#
#
# def create_event(summary, start, end, invite, description):
#     event = {
#         'summary': summary,
#         'description': description,
#         'start': start,
#         'end': end,
#         'attendees': [
#             {'email': invite},
#         ],
#     }
#
#     return service.events().insert(calendarId='primary', body=event, sendNotifications=True).execute()
#
#
# create_event("Pizza", "11-11-2011 11:11:11", "11-12-2011 11:11:11", None, "meeting about pizza")  # callfunction
