from datetime import datetime, timedelta

from gauth import authenticate_google_calendar


def create_event(service, summary, start_date, calendar_id="primary"):
    event = {
        "summary": summary,
        "start": {"date": start_date, "timeZone": "UTC"},
        "end": {"date": start_date, "timeZone": "UTC"},
        "reminders": {
            "useDefault": False,
            "overrides": [{"method": "popup", "minutes": 0}],
        },
    }
    service.events().insert(calendarId=calendar_id, body=event).execute()


def main():
    # User-defined start date (YYYY-MM-DD)
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    # Authenticate and initialize Google Calendar API
    service = authenticate_google_calendar()

    # Create events for 100-day anniversaries
    for days in range(100, 1000 + 1, 100):  # 100 to 1000 days
        anniversary_date = start_date + timedelta(days=days)
        create_event(
            service, f"🖤 {days}-Day Anniversary", anniversary_date.strftime("%Y-%m-%d")
        )
        print(
            f'Created 🖤 {days}-Day Anniversary on {anniversary_date.strftime("%Y-%m-%d")}'
        )

    # Create events for yearly anniversaries
    for years in range(1, 10 + 1):  # 1 to 10 years
        anniversary_date = start_date.replace(year=start_date.year + years)
        create_event(
            service,
            f"🖤 {years}-Year Anniversary",
            anniversary_date.strftime("%Y-%m-%d"),
        )
        print(
            f'Created 🖤 {years}-Year Anniversary on {anniversary_date.strftime("%Y-%m-%d")}'
        )


if __name__ == "__main__":
    main()
