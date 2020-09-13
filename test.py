import requests

BASE = "http://127.0.0.1:5000/"

event = {"name": "event name", "description": "cool event", "meeting_link": "link",
         "donation_amount": 45.45, "event_date": "5/5/5", "user_id": 55}

event2 = {"name": "event name2", "description": "cool event2", "meeting_link": "link2",
         "donation_amount": 45.55, "event_date": "5/6/5", "user_id": 57}

response = requests.put(BASE + "event/1", event)
response2 = requests.put(BASE + "events/2", event2)


response_get = requests.get(BASE + "/events")
print(response_get.json())
