import requests

BASE = "http://127.0.0.1:5000/"

event = {"name": "event name", "description": "cool event", "meeting_link": "link",
         "donation_amount": 45.45, "event_date": "5/5/5", "user_id": 55}

response = requests.put(BASE + "event/1", event)

response_get = requests.get(BASE+ "event/1")

print(response_get.json())