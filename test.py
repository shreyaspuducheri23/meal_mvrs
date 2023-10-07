import requests
import pandas as pd

api_key = "AIzaSyCV9qBojjy4U4COvHlg6YFxL9uUkqBfjpQ"

def get_coordinates(address, api_key):
    """Get latitude and longitude for a given address using Google Maps API."""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        return latitude, longitude
    else:
        return None, None

def get_municipality(latitude, longitude, api_key):
    """Get the municipality for a given latitude and longitude using Google Maps API."""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        # Parse the address components to find the municipality (also known as 'locality' in Google's terms)
        for component in data['results'][0]['address_components']:
            if 'locality' in component['types']:
                return component['long_name']
    return None


food_bank_df = pd.read_csv("Food Bank List.csv")


print(food_bank_df.dtypes)
