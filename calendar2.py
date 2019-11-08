"""Code adapted from https://gist.github.com/nikhilkumarsingh/8a88be71243afe8d69390749d16c8322"""
import pickle
import pprint

import pip
import google_auth_oauthlib
import googleapiclient

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import *
from main import *


scopes = ['https://www.googleapis.com/auth/calendar'] # access to calendar in mode read/write

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes =scopes)
credentials = flow.run_console()