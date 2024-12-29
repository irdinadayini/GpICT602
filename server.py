from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.get_json()  # Get the data sent by the Android app
    username = data.get('username')
    lat = data.get('latitude')
    lng = data.get('longitude')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Here, you can store the data in a database or log it
    print(f"User: {username}, Location: {lat}, {lng}, Time: {timestamp}")
    
    return {"message": "Location received successfully!"}, 200

if __name__ == "__main__":
    app.run(debug=True)
