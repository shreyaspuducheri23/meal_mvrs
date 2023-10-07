from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store excess food items (for demonstration, you might want to use a database in production)
excess_food_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_food', methods=['POST'])
def store_food():
    data = request.json
    food_item = data.get('food_item')
    
    # Store the food item (you can also store it in a database)
    excess_food_items.append(food_item)
    
    return jsonify({"message": f"Excess food item {food_item} stored successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Running on a different port to avoid conflict with the first app
