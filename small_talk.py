API_KEY = 'n4JgSSH8QleMqTDFkAzWbw'
API_SECRET= 'n7tL5F2ILaY3NW2GJ1i2V3aLmdEuXRwjb42x'

from pyzoom import ZoomClient
from datetime import datetime as dt

def start_conversation():
    client = ZoomClient(API_KEY, API_SECRET)
    meeting = client.meetings.create_meeting('new', start_time=dt.now().isoformat(), duration_min=60, password='not-secure')
    return meeting.start_url



