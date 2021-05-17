from __future__ import print_function
import datetime
import pickle
import json
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)





    with open('data.json') as f:
        data = json.load(f)

    name = input('input the guys: ')
    # find the number of events that the person has
    num_events = len(data["__collections__"]["successfulPeople"][name]["__collections__"])

    for i in range(1, num_events + 1):
        person = data["__collections__"]["successfulPeople"][name]["__collections__"]["event" + str(i)]
        key = list(person)[0]
        if "00:00:00" in datetime.datetime.utcfromtimestamp(person[key]['startTime']['value']['_seconds']).strftime('%H:%M:%SZ') or  "00:00:00" in datetime.datetime.utcfromtimestamp(person[key]['endTime']['value']['_seconds']).strftime('%H:%M:%SZ'):
            pass
        start = datetime.datetime.utcnow().strftime('%Y-%m-%dT') + datetime.datetime.utcfromtimestamp(person[key]['startTime']['value']['_seconds']).strftime('%H:%M:%SZ')
        end = datetime.datetime.utcnow().strftime('%Y-%m-%dT') + datetime.datetime.utcfromtimestamp(person[key]['endTime']['value']['_seconds']).strftime('%H:%M:%SZ')
        if start>end:
            pass
        event = {
            # make querey for summary
            'summary': person[key]['activity'],
            # make querey for description
            'description': person[key]['description'],
            'start': {
                # import time
                'dateTime': start,
                'timeZone': 'Canada/Eastern',
            },
            # make querey for time
            'end': {
                # import time
                'dateTime': end,
                'timeZone': 'Canada/Eastern',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY'
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 20}
                ],
            },
        }
        event = service.events().insert(calendarId=data["__collections__"]["successfulPeople"][name]["id"], body=event).execute()

if __name__ == '__main__':
    main()