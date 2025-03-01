def detect_anomalies(sensor_data):
    anomalies = []

    # Example: Detect high temperature
    if sensor_data.get('temperature', 0) > 40:
        anomalies.append('High temperature detected')

    # Example: Detect low humidity
    if sensor_data.get('humidity', 0) < 20:
        anomalies.append('Low humidity detected')

    # Example: Detect no motion (chicks might be inactive)
    if sensor_data.get('motion', 0) == 0:
        anomalies.append('No motion detected')

    return anomalies
