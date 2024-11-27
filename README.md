### Steps to Set Up:
1. **Enable Google Calendar API**: Go to the [Google Cloud Console](https://console.cloud.google.com/), create a project, and enable the Google Calendar API.
2. **Obtain OAuth Credentials**: Download the credentials JSON file, save it as `credentials.json`.
3. **Install Required Libraries**: Install `google-auth`, `google-auth-oauthlib`, and `google-api-python-client`:
   ```bash
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```
4. **Run the Script**: `main.py`

### How It Works:
1. **Start Date**: Prompts you to input the start date of the anniversary series.
2. **100-Day Anniversaries**: Creates events at 100-day intervals up to 1000 days.
3. **Yearly Anniversaries**: Creates events for each year up to 10 years.

### Notes:
- The script creates events in your primary calendar. Change the `calendar_id` if needed.
- Ensure your Python environment has internet access and Google authentication is set up properly.