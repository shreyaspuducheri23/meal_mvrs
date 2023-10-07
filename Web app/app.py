from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

def euclidean_distance(lat1, lon1, lat2, lon2):
    # Conversion factor to convert degrees to meters: 111,139 meters per degree
    conversion_factor = 111139  
    
    # Calculate differences in latitude and longitude
    dlat = (lat2 - lat1) * conversion_factor
    dlon = (lon2 - lon1) * conversion_factor
    
    # Euclidean distance formula
    distance = np.sqrt(dlat**2 + dlon**2)
    
    return distance

def closest_food_bank(user_lat, user_lon):
    food_banks_df = pd.read_csv("food_bank_data_with_xy.csv", usecols=["Name", "Latitude", "Longitude"])
    food_banks_df['distance_to_user'] = food_banks_df.apply(
        lambda row: euclidean_distance(user_lat, user_lon, row['Latitude'], row['Longitude']), axis=1)

    # Find the row of the closest food bank
    closest_food_bank_row = food_banks_df.loc[food_banks_df['distance_to_user'].idxmin()]
    
    # Convert the row to a tuple
    closest_food_bank_tuple = tuple(closest_food_bank_row)
    
    return closest_food_bank_tuple

app = Flask(__name__)
closest_food_bank_loc = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_location', methods=['POST'])
def store_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    closest_food_bank_loc = closest_food_bank(latitude, longitude)
    
    return jsonify({
        "message": "closest food bank is " + closest_food_bank_loc[0],
        "closest_food_bank_latitude": closest_food_bank_loc[1],
        "closest_food_bank_longitude": closest_food_bank_loc[2]
    })


if __name__ == '__main__':
    app.run(debug=True)

