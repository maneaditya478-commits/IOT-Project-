"""
Predictive Worker Safety Helmet - Supervisory Central Monitoring Dashboard
Flask Web Server providing real-time telemetry ingestion, interactive worker status,
predictive risk scoring gauges, alert dispatching, and dynamic map tracking.
"""

from flask import Flask, render_template_string, request, jsonify
import random
import time
from datetime import datetime

app = Flask(__name__)

# In-memory storage for active workers
workers_state = {
    "WRK-VIT-40": {
        "name": "Sail Sitaram Nagale",
        "role": "Scaffold Technician",
        "location_name": "Sector 4 - High Rise Tower A",
        "lat": 18.4636,
        "lng": 73.8682,
        "temperature": 27.4,
        "delta_temp": 0.1,
        "gas_ppm": 14.2,
        "heart_rate": 78,
        "accel_mag": 1.02,
        "jerk": 0.25,
        "risk_score": 14,
        "risk_level": "Low Risk",
        "last_update": datetime.now().strftime("%H:%M:%S"),
        "status": "NORMAL"
    },
    "WRK-VIT-12": {
        "name": "Rohan Sharma",
        "role": "Excavation Operator",
        "location_name": "Sector 1 - Deep Trench B",
        "lat": 18.4642,
        "lng": 73.8690,
        "temperature": 39.8,
        "delta_temp": 1.2,
        "gas_ppm": 42.0,
        "heart_rate": 128,
        "accel_mag": 1.15,
        "jerk": 0.40,
        "risk_score": 68,
        "risk_level": "Medium Risk",
        "last_update": datetime.now().strftime("%H:%M:%S"),
        "status": "HEAT_GAS_ADVISORY"
    }
}

alerts_log = [
    {
        "time": datetime.now().strftime("%H:%M:%S"),
        "worker_id": "WRK-VIT-12",
        "type": "ELEVATED_HEAT_AND_GAS",
        "message": "Worker exhibiting cardiac stress with rising ambient temperature (39.8°C) and Gas (42 PPM).",
        "severity": "Medium"
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Predictive Worker Safety Helmet - IoT & ML Command Center</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .navbar { background-color: #161b22; border-bottom: 1px solid #30363d; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; margin-bottom: 20px; }
        .card-header { background-color: #21262d; border-bottom: 1px solid #30363d; font-weight: 600; }
        .badge-low { background-color: #238636; color: #fff; }
        .badge-medium { background-color: #d29922; color: #000; }
        .badge-high { background-color: #da3633; color: #fff; }
        .stat-box { padding: 15px; border-radius: 6px; background-color: #21262d; text-align: center; }
        .stat-val { font-size: 1.8rem; font-weight: 700; }
        .stat-lbl { font-size: 0.85rem; color: #8b949e; text-transform: uppercase; }
        .table-dark-custom { background-color: #161b22; color: #c9d1d9; }
        .alert-item { border-left: 4px solid #da3633; background-color: #21262d; padding: 10px 15px; margin-bottom: 8px; border-radius: 4px; }
        .gauge-bar { height: 12px; border-radius: 6px; background-color: #30363d; overflow: hidden; margin-top: 8px; }
        .gauge-fill { height: 100%; transition: width 0.5s ease; }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark px-4 py-3">
        <span class="navbar-brand mb-0 h1 d-flex align-items-center">
            <i class="fa-solid fa-helmet-safety text-warning me-3 fs-3"></i>
            <div>
                <div>Predictive Worker Safety Helmet — IoT & ML Command Center</div>
                <small class="text-secondary fs-6">Patent Reference System • Vishwakarma Institute of Technology</small>
            </div>
        </span>
        <div>
            <span class="badge bg-success me-2"><i class="fa-solid fa-signal me-1"></i> LoRa / Wi-Fi Gateway Online</span>
            <span class="badge bg-info text-dark"><i class="fa-solid fa-microchip me-1"></i> Edge ML Active</span>
        </div>
    </nav>

    <div class="container-fluid py-4 px-4">
        <!-- Top Stats Row -->
        <div class="row g-3 mb-4">
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-primary" id="total-workers">2</div>
                    <div class="stat-lbl">Active Smart Helmets</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-success" id="safe-workers">1</div>
                    <div class="stat-lbl">Safe / Low Risk</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-warning" id="advisory-workers">1</div>
                    <div class="stat-lbl">Advisories (Medium Risk)</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-danger" id="critical-workers">0</div>
                    <div class="stat-lbl">Critical Incidents (High Risk)</div>
                </div>
            </div>
        </div>

        <div class="row">
            <!-- Worker Details & Telemetry Cards -->
            <div class="col-lg-8">
                <div class="card">
                    <div class="card-header d-flex justify-content-between align-items-center">
                        <span><i class="fa-solid fa-users-gear me-2"></i> Real-Time Telemetry & Risk Score Index</span>
                        <div class="btn-group">
                            <button class="btn btn-sm btn-outline-danger" onclick="triggerSim('fall')"><i class="fa-solid fa-triangle-exclamation me-1"></i> Simulate Fall</button>
                            <button class="btn btn-sm btn-outline-warning" onclick="triggerSim('gas')"><i class="fa-solid fa-biohazard me-1"></i> Simulate Gas Leak</button>
                            <button class="btn btn-sm btn-outline-success" onclick="triggerSim('reset')"><i class="fa-solid fa-rotate-left me-1"></i> Reset Baseline</button>
                        </div>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-dark table-hover mb-0 align-middle">
                                <thead>
                                    <tr>
                                        <th>Worker</th>
                                        <th>Biometrics & Motion</th>
                                        <th>Environment</th>
                                        <th>GPS Location</th>
                                        <th>ML Risk Score</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody id="workers-table-body">
                                    <!-- Dynamic rows loaded via JS -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- Simulation Controls and Architecture Info -->
                <div class="card">
                    <div class="card-header">
                        <i class="fa-solid fa-diagram-project me-2"></i> Predictive Multi-Sensor Fusion Workflow
                    </div>
                    <div class="card-body">
                        <div class="row text-center">
                            <div class="col-md-3 mb-2">
                                <div class="p-2 border border-secondary rounded">
                                    <i class="fa-solid fa-microchip text-primary fs-4 mb-2"></i>
                                    <h6>1. Edge Acquisition</h6>
                                    <small class="text-secondary">ESP32, IMU 50Hz, Gas, Temp, PPG Heart Rate</small>
                                </div>
                            </div>
                            <div class="col-md-3 mb-2">
                                <div class="p-2 border border-secondary rounded">
                                    <i class="fa-solid fa-filter text-info fs-4 mb-2"></i>
                                    <h6>2. Noise Filtering</h6>
                                    <small class="text-secondary">Median filter, Jerk derivation & artifact removal</small>
                                </div>
                            </div>
                            <div class="col-md-3 mb-2">
                                <div class="p-2 border border-secondary rounded">
                                    <i class="fa-solid fa-brain text-warning fs-4 mb-2"></i>
                                    <h6>3. ML Risk Model</h6>
                                    <small class="text-secondary">Random Forest Regressor / Classifier (0-100 Score)</small>
                                </div>
                            </div>
                            <div class="col-md-3 mb-2">
                                <div class="p-2 border border-secondary rounded">
                                    <i class="fa-solid fa-tower-broadcast text-danger fs-4 mb-2"></i>
                                    <h6>4. Dual-Action Alert</h6>
                                    <small class="text-secondary">Local Buzzer/LED + LoRa Telemetry Dispatch</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Side Alerts & Map Feed -->
            <div class="col-lg-4">
                <div class="card">
                    <div class="card-header d-flex justify-content-between align-items-center">
                        <span><i class="fa-solid fa-bell me-2"></i> Live Incident & Alert Feed</span>
                        <span class="badge bg-danger" id="alert-count">1</span>
                    </div>
                    <div class="card-body" style="max-height: 400px; overflow-y: auto;" id="alerts-container">
                        <!-- Alerts dynamically populated -->
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">
                        <i class="fa-solid fa-map-location-dot me-2"></i> Industrial Geo-Fence Tracking
                    </div>
                    <div class="card-body">
                        <div class="p-3 bg-dark rounded border border-secondary text-center">
                            <i class="fa-solid fa-location-crosshairs text-success fs-1 mb-2"></i>
                            <h6>Site: Pune Industrial Infrastructure Zone</h6>
                            <p class="small text-secondary mb-1">GPS Coordinates: 18.4636° N, 73.8682° E</p>
                            <span class="badge bg-primary">All Units Geotagged via Onboard GPS (106)</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function updateDashboard() {
            fetch('/api/state')
                .then(res => res.json())
                .then(data => {
                    const tbody = document.getElementById('workers-table-body');
                    tbody.innerHTML = '';
                    
                    let lowCount = 0, medCount = 0, highCount = 0;
                    
                    for (const [id, w] of Object.entries(data.workers)) {
                        let badgeClass = 'badge-low';
                        let fillClass = 'bg-success';
                        if (w.risk_score >= 75) {
                            badgeClass = 'badge-high';
                            fillClass = 'bg-danger';
                            highCount++;
                        } else if (w.risk_score >= 40) {
                            badgeClass = 'badge-medium';
                            fillClass = 'bg-warning';
                            medCount++;
                        } else {
                            lowCount++;
                        }
                        
                        const row = `
                            <tr>
                                <td>
                                    <strong>${w.name}</strong><br>
                                    <small class="text-secondary">${id} • ${w.role}</small>
                                </td>
                                <td>
                                    <div><i class="fa-solid fa-heart-pulse text-danger me-1"></i> ${w.heart_rate} BPM</div>
                                    <small class="text-secondary">Accel: ${w.accel_mag}g | Jerk: ${w.jerk}g/s</small>
                                </td>
                                <td>
                                    <div><i class="fa-solid fa-temperature-three-quarters text-warning me-1"></i> ${w.temperature}°C</div>
                                    <small class="text-secondary">Toxic Gas: ${w.gas_ppm} PPM</small>
                                </td>
                                <td>
                                    <i class="fa-solid fa-location-dot text-info me-1"></i> ${w.location_name}<br>
                                    <small class="text-secondary">${w.lat.toFixed(4)}, ${w.lng.toFixed(4)}</small>
                                </td>
                                <td style="min-width: 150px;">
                                    <div class="d-flex justify-content-between align-items-center">
                                        <span class="fw-bold">${w.risk_score}/100</span>
                                        <span class="badge ${badgeClass}">${w.risk_level}</span>
                                    </div>
                                    <div class="gauge-bar">
                                        <div class="gauge-fill ${fillClass}" style="width: ${w.risk_score}%;"></div>
                                    </div>
                                </td>
                                <td>
                                    <span class="badge ${w.risk_score >= 75 ? 'bg-danger' : (w.risk_score >= 40 ? 'bg-warning text-dark' : 'bg-success')}">
                                        ${w.status}
                                    </span>
                                </td>
                            </tr>
                        `;
                        tbody.innerHTML += row;
                    }
                    
                    document.getElementById('total-workers').innerText = Object.keys(data.workers).length;
                    document.getElementById('safe-workers').innerText = lowCount;
                    document.getElementById('advisory-workers').innerText = medCount;
                    document.getElementById('critical-workers').innerText = highCount;
                    
                    // Render Alerts
                    const alertsDiv = document.getElementById('alerts-container');
                    alertsDiv.innerHTML = '';
                    document.getElementById('alert-count').innerText = data.alerts.length;
                    data.alerts.slice().reverse().forEach(a => {
                        const alertHtml = `
                            <div class="alert-item" style="border-left-color: ${a.severity === 'High' ? '#da3633' : '#d29922'};">
                                <div class="d-flex justify-content-between">
                                    <strong class="text-${a.severity === 'High' ? 'danger' : 'warning'}"><i class="fa-solid fa-triangle-exclamation me-1"></i> ${a.type}</strong>
                                    <small class="text-secondary">${a.time}</small>
                                </div>
                                <div class="small mt-1">${a.message}</div>
                                <small class="text-info mt-1 d-block"><i class="fa-solid fa-id-badge me-1"></i> Target: ${a.worker_id}</small>
                            </div>
                        `;
                        alertsDiv.innerHTML += alertHtml;
                    });
                });
        }

        function triggerSim(action) {
            fetch('/api/simulate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: action })
            }).then(() => updateDashboard());
        }

        setInterval(updateDashboard, 2000);
        updateDashboard();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/state')
def get_state():
    return jsonify({
        "workers": workers_state,
        "alerts": alerts_log
    })

@app.route('/api/telemetry', methods=['POST'])
def receive_telemetry():
    data = request.json or {}
    worker_id = data.get('worker_id', 'WRK-VIT-40')
    if worker_id in workers_state:
        workers_state[worker_id].update({
            "temperature": data.get('temperature', workers_state[worker_id]['temperature']),
            "gas_ppm": data.get('gas_ppm', workers_state[worker_id]['gas_ppm']),
            "heart_rate": data.get('heart_rate', workers_state[worker_id]['heart_rate']),
            "accel_mag": data.get('accel_mag', workers_state[worker_id]['accel_mag']),
            "jerk": data.get('jerk', workers_state[worker_id]['jerk']),
            "risk_score": data.get('risk_score', workers_state[worker_id]['risk_score']),
            "risk_level": data.get('risk_level', workers_state[worker_id]['risk_level']),
            "last_update": datetime.now().strftime("%H:%M:%S")
        })
    return jsonify({"status": "SUCCESS", "message": "Telemetry processed"})

@app.route('/api/simulate', methods=['POST'])
def simulate_event():
    req = request.json or {}
    action = req.get('action')
    
    if action == 'fall':
        workers_state["WRK-VIT-40"].update({
            "accel_mag": 5.4,
            "jerk": 48.0,
            "heart_rate": 142,
            "risk_score": 96,
            "risk_level": "High Risk",
            "status": "CRITICAL_FALL_IMPACT",
            "last_update": datetime.now().strftime("%H:%M:%S")
        })
        alerts_log.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "worker_id": "WRK-VIT-40",
            "type": "FREE-FALL & IMPACT DETECTED",
            "message": "High-g impact (5.4g) and high jerk detected on helmet. Worker motionless. Immediate dispatch required!",
            "severity": "High"
        })
    elif action == 'gas':
        workers_state["WRK-VIT-40"].update({
            "gas_ppm": 88.5,
            "temperature": 41.2,
            "heart_rate": 135,
            "risk_score": 89,
            "risk_level": "High Risk",
            "status": "CRITICAL_GAS_LEAK",
            "last_update": datetime.now().strftime("%H:%M:%S")
        })
        alerts_log.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "worker_id": "WRK-VIT-40",
            "type": "HAZARDOUS GAS BURST",
            "message": "Toxic gas level exceeded safety threshold (88.5 PPM). Worker in immediate danger zone!",
            "severity": "High"
        })
    elif action == 'reset':
        workers_state["WRK-VIT-40"].update({
            "temperature": 27.4,
            "delta_temp": 0.1,
            "gas_ppm": 14.2,
            "heart_rate": 78,
            "accel_mag": 1.02,
            "jerk": 0.25,
            "risk_score": 14,
            "risk_level": "Low Risk",
            "status": "NORMAL",
            "last_update": datetime.now().strftime("%H:%M:%S")
        })
    return jsonify({"status": "SUCCESS"})

if __name__ == '__main__':
    print("Starting Supervisory Command Dashboard on http://localhost:5000 ...")
    app.run(host='0.0.0.0', port=5000, debug=False)
