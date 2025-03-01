// Fetch sensor data and update the dashboard
async function fetchSensorData() {
  const response = await fetch('http://localhost:5000/api/sensors/data');
  const data = await response.json();

  // Update sensor data
  document.getElementById('temperature').textContent = data.temperature || '--';
  document.getElementById('humidity').textContent = data.humidity || '--';
  document.getElementById('motion').textContent = data.motion || '--';

  // Check for anomalies
  const anomalyResponse = await fetch('http://localhost:5000/api/detect-anomalies', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const anomalies = await anomalyResponse.json();

  // Display anomalies
  const anomaliesList = document.getElementById('anomalies-list');
  anomaliesList.innerHTML = anomalies.map(anomaly => `<li>${anomaly}</li>`).join('');
}

// Refresh data every 5 seconds
setInterval(fetchSensorData, 5000);
fetchSensorData();
