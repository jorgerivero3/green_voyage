from typing import List, Optional
import openrouteservice
from app.services.time_formatter import time_formatter
from app.services.carbon_service import calculate_carbon
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

#TODO: Make this an env file before pushing anything to Github.
API_KEY = os.getenv("OPEN_ROUTE_KEY")
open_client = openrouteservice.Client(key=API_KEY)

def calculate_route(stops: List[str], filters: Optional[List[str]] = None) -> dict:
    
    exclusions = set(filters) if filters else set()

    #Gather coordinates for stops in request
    coordinates = []
    for stop in stops:
        response = open_client.pelias_search(stop)
        details = response["features"][0]["geometry"]["coordinates"]
        coordinates.append(details)
   
    #TODO: Error handling for empty response lists []
    #TODO: make convert_time()
    #TODO: See if you can request only the needed fields

    #Directions code
    # directions_result = open_client.directions(coordinates)
    # directions = []
    # for i in range(len(coordinates) - 1):
    #     coor_to_from = [coordinates[i], coordinates[i+1]]
    #     directions_result = open_client.directions(coordinates=coor_to_from)
    #     directions.append(directions_result)
    
    #Matrix code
    matrix = open_client.distance_matrix(locations=coordinates, metrics=["distance", "duration"])
    distances_matrix = matrix["distances"]
    times = matrix["durations"]

    distances = []
    for i in range(len(distances_matrix) - 1):
        distance = distances_matrix[i][i + 1]
        distance = distance / 1000
        distances.append(distance)
    
    travel_times = []
    for i in range(len(times) - 1):
        time = times[i][i + 1]
        #Converts to minutes or hours
        time_str = time_formatter(time)
        travel_times.append(time_str)

    carbon_response = calculate_carbon(distances[0])


    return {
        "stops": stops, 
        # "filters_applied": list(exclusions), 
        # "message": "Here are the coordinates!",
        # "coordinates": coordinates,
        # "matrix": matrix,
        "travel_times": travel_times,
        "distances": distances,
        "carbon": carbon_response
    }