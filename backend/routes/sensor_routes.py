from flask import Blueprint, request, jsonify
from database.db import get_db
from models.sensor_data import SensorData

sensor_routes = Blueprint('sensor_routes', __name__)

# Save sensor data
@sensor_routes.route('/data', methods=['POST'])
def save_sensor_data():
    data = request.json
    db = get_db()
    sensor_data = SensorData(
        temperature=data['temperature'],
        humidity=data['humidity'],
        motion=data['motion']
    )
    db.add(sensor_data)
    db.commit()
    return jsonify({'message': 'Sensor data saved successfully'}), 201

# Get all sensor data
@sensor_routes.route('/data', methods=['GET'])
def get_sensor_data():
    db = get_db()
    sensor_data = db.query(SensorData).all()
    return jsonify([{
        'temperature': data.temperature,
        'humidity': data.humidity,
        'motion': data.motion,
        'timestamp': data.timestamp
    } for data in sensor_data])
