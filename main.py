import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('.env')

USERNAME = os.getenv('PIXELA_USERNAME')
TOKEN = os.getenv('TOKEN')

print(USERNAME)
print(TOKEN)


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Workout Tracker",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30"
}

response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
