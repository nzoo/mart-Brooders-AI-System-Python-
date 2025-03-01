from flask import Flask, jsonify, request
from database.db import init_db
from routes.sensor_routes import sensor_routes
from ai_model.anomaly_detection import detect_anomalies

app = Flask(__name__)
app.config['DATABASE'] = 'smart_brooders.db'

# Initialize the database
init_db(app)

# Register routes
app.register_blueprint(sensor_routes)

# AI Anomaly Detection Endpoint
@app.route('/api/detect-anomalies', methods=['POST'])
def detect_anomalies_endpoint():
    sensor_data = request.json
    anomalies = detect_anomalies(sensor_data)
    return jsonify({'anomalies': anomalies})

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
