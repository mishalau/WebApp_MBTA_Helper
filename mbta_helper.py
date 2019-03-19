# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "4hQccvGhtkRNlSh8G5QUQqkXGJpnlA4d"
MBTA_API_KEY = "172ce4d9fbbe422496368d3b1ead4e18"

# A little bit of scaffolding if you want to use it

import requests
from urllib.request import urlopen
import json
from flask import Flask

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data


def get_lat_long(Location):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = '{}?key={}&location={}'.format(MAPQUEST_BASE_URL, MAPQUEST_API_KEY, Location)
    print (url)
    data = get_json(url)
    import pprint
    latitude=data["results"][0]["locations"][0]["displayLatLng"]["lat"]
    longitude=data["results"][0]["locations"][0]["displayLatLng"]["lng"]
    return [latitude, longitude]


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url="https://api-v3.mbta.com/stops?sort=distance&filter[latitude]={latitude}&filter[longitude]={longitude}".format(longitude=longitude, latitude=latitude)
    data=get_json(url)
    return (data['data'][0]['attributes']['name'], data['data'][0]['attributes']['wheelchair_boarding'])



def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_lon= get_lat_long(place_name)
    latitude=lat_lon[0]
    longitude=lat_lon[1]
    return get_nearest_station(latitude, longitude)


def main(Location):
    """
    You can call the functions here
    """

    return find_stop_near(Location)


if __name__ == '__main__':
    main(Location)