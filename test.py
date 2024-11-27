import json

from gauth import authenticate_google_calendar

# Authenticate and initialize Google Calendar API
service = authenticate_google_calendar()

del_event_ids = []

page_token = None
while True:
    events = service.events().list(calendarId="primary", pageToken=page_token).execute()
    for event in events["items"]:
        if "summary" in event and "anniversary" in event["summary"].lower():
            print(event["summary"], "on", event["start"]["date"])
            if input("Delete?: ").lower().startswith("y"):
                del_event_ids.append(event["id"])
                print("Deleted", event["summary"], "on", event["start"]["date"])
            # print(json.dumps(event, indent=2))
            print()
    page_token = events.get("nextPageToken")
    if not page_token:
        break


for _id in del_event_ids:
    service.events().delete(calendarId="primary", eventId=_id).execute()
