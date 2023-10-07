from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store geolocation data (for demonstration purposes, in a production application you'd use a database)
geolocation_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_location', methods=['POST'])
def store_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Store the data (you can also store it in a database)
    geolocation_data['latitude'] = latitude
    geolocation_data['longitude'] = longitude
    
    return jsonify({"message": "Location stored successfully"})

if __name__ == '__main__':
    app.run(debug=True)
