from __future__ import print_function

import datetime
import os.path
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def getCalender():
    maxEvents = 20
    #Gets the next 10 events from Google Calendar API
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        print('Getting the upcoming ' + str(maxEvents) + ' events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=maxEvents, singleEvents=True,
                                              orderBy='startTime', timeZone = 'Canada/Eastern').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return "No Events Scheduled"


        allEvents = ""

        # Reformats events into a more readable format for the assistant
        #Also removes UTC time
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            

            start = re.sub(":00-[0-9][0-9]:00","",start)
            start = re.sub("T", " ", start)

            end = re.sub(":00-[0-9][0-9]:00","",end)
            end = re.sub("T", " ", end)

            allEvents += (start + " - " + end + "\t "+ event['summary'] +"\n")

        return allEvents

    except HttpError as error:
        print('An error occurred: %s' % error)