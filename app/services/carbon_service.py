from typing import List, Optional
import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_KEY = API_KEY = os.getenv("CARBON_KEY")
URL = "https://www.carboninterface.com/api/v1"

def calculate_carbon(distance):
    print(distance)
    path = "/estimates"
    url = URL + path
    headers = {"Authorization": "Bearer " + API_KEY}
    data = {
        "type": "vehicle",
        "distance_unit": "km", 
        "distance_value": distance,
        "vehicle_model_id": "7268a9b7-17e8-4c8d-acca-57059252afe9"
    }

    r = requests.post(url, headers=headers, json=data)
    print(r.request.headers, r.request.body, r.request)
    return r.json()

    #TODO: Handle status codes that are not 200 
