import os
from datetime import datetime
from flask import Flask, render_template_string, request, jsonify, send_from_directory

app = Flask(__name__)

# In-memory storage for active workers
workers_state = {
    "WRK-VIT-40": {
        "name": "Sail Sitaram Nagale",
        "role": "Scaffold Structural Lead",
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
        "lat": 18.4652,
        "lng": 73.8701,
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
    },
    "WRK-VIT-07": {
        "name": "Amit Deshmukh",
        "role": "Welding Specialist",
        "location_name": "Sector 2 - Pipe Assembly",
        "lat": 18.4628,
        "lng": 73.8665,
        "temperature": 31.0,
        "delta_temp": 0.3,
        "gas_ppm": 18.5,
        "heart_rate": 84,
        "accel_mag": 0.98,
        "jerk": 0.15,
        "risk_score": 22,
        "risk_level": "Low Risk",
        "last_update": datetime.now().strftime("%H:%M:%S"),
        "status": "NORMAL"
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
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Leaflet CSS for Map -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --bg-dark: #0d1117;
            --card-bg: #161b22;
            --card-header: #21262d;
            --border-color: #30363d;
            --text-main: #c9d1d9;
            --accent-green: #238636;
            --accent-yellow: #d29922;
            --accent-red: #da3633;
            --accent-blue: #58a6ff;
        }
        body { 
            background-color: var(--bg-dark); 
            color: var(--text-main); 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
        }
        .navbar { 
            background-color: var(--card-bg); 
            border-bottom: 1px solid var(--border-color); 
        }
        .card { 
            background-color: var(--card-bg); 
            border: 1px solid var(--border-color); 
            border-radius: 8px; 
            margin-bottom: 20px; 
        }
        .card-header { 
            background-color: var(--card-header); 
            border-bottom: 1px solid var(--border-color); 
            font-weight: 600; 
        }
        .stat-box { 
            padding: 18px; 
            border-radius: 8px; 
            background-color: var(--card-header); 
            border: 1px solid var(--border-color); 
            text-align: center; 
        }
        .stat-val { font-size: 2rem; font-weight: 700; }
        .stat-lbl { font-size: 0.82rem; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; }
        .badge-low { background-color: var(--accent-green); color: #fff; }
        .badge-medium { background-color: var(--accent-yellow); color: #000; }
        .badge-high { background-color: var(--accent-red); color: #fff; }
        .alert-item { 
            border-left: 4px solid var(--accent-red); 
            background-color: var(--card-header); 
            padding: 12px 14px; 
            margin-bottom: 10px; 
            border-radius: 4px; 
        }
        .gauge-bar { 
            height: 10px; 
            border-radius: 5px; 
            background-color: #30363d; 
            overflow: hidden; 
            margin-top: 6px; 
        }
        .gauge-fill { height: 100%; transition: width 0.4s ease; }
        #map { height: 340px; border-radius: 6px; }
        .btn-sim { font-weight: 500; font-size: 0.85rem; }
    </style>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-dark px-4 py-3 sticky-top shadow-sm">
        <span class="navbar-brand mb-0 h1 d-flex align-items-center">
            <i class="fa-solid fa-helmet-safety text-warning me-3 fs-2"></i>
            <div>
                <div class="fw-bold fs-5">Predictive Worker Safety Helmet — Command Center</div>
                <small class="text-secondary" style="font-size: 0.78rem;">IoT Multi-Sensor Fusion & Edge Machine Learning • VIT Pune Patent Reference</small>
            </div>
        </span>
        <div class="d-flex align-items-center gap-2">
            <button class="btn btn-sm btn-outline-info" data-bs-toggle="modal" data-bs-target="#patentModal">
                <i class="fa-solid fa-file-contract me-1"></i> View Patent CAD Drawings
            </button>
            <span class="badge bg-success px-3 py-2"><i class="fa-solid fa-tower-broadcast me-1"></i> LoRa / Wi-Fi Active</span>
            <span class="badge bg-primary px-3 py-2"><i class="fa-solid fa-brain me-1"></i> Edge ML Online</span>
        </div>
    </nav>

    <div class="container-fluid py-4 px-4">
        <!-- Top Stats Row -->
        <div class="row g-3 mb-4">
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-primary" id="total-workers">3</div>
                    <div class="stat-lbl">Active Smart Helmets</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-success" id="safe-workers">2</div>
                    <div class="stat-lbl">Safe (Low Risk: 0–39)</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-warning" id="advisory-workers">1</div>
                    <div class="stat-lbl">Advisory (Medium Risk: 40–74)</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-box">
                    <div class="stat-val text-danger" id="critical-workers">0</div>
                    <div class="stat-lbl">Critical Incidents (High: 75–100)</div>
                </div>
            </div>
        </div>

        <!-- Main Content Area -->
        <div class="row">
            <!-- Left Column: Table & Sensor Charts -->
            <div class="col-lg-8">
                <!-- Real-Time Telemetry Table -->
                <div class="card shadow-sm">
                    <div class="card-header d-flex justify-content-between align-items-center flex-wrap gap-2">
                        <span><i class="fa-solid fa-microchip me-2 text-info"></i> Real-Time Multi-Sensor Telemetry & Risk Index</span>
                        <div class="btn-group flex-wrap">
                            <button class="btn btn-sm btn-outline-danger btn-sim" onclick="triggerSim('fall')">
                                <i class="fa-solid fa-person-falling me-1"></i> Fall & Impact
                            </button>
                            <button class="btn btn-sm btn-outline-warning btn-sim" onclick="triggerSim('gas')">
                                <i class="fa-solid fa-biohazard me-1"></i> Gas Leak
                            </button>
                            <button class="btn btn-sm btn-outline-danger btn-sim" onclick="triggerSim('heat')">
                                <i class="fa-solid fa-temperature-arrow-up me-1"></i> Heat Stress
                            </button>
                            <button class="btn btn-sm btn-outline-success btn-sim" onclick="triggerSim('reset')">
                                <i class="fa-solid fa-rotate-left me-1"></i> Reset Baseline
                            </button>
                        </div>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-dark table-hover mb-0 align-middle">
                                <thead>
                                    <tr class="text-secondary small">
                                        <th>WORKER & ID</th>
                                        <th>PHYSIOLOGY & MOTION</th>
                                        <th>ENVIRONMENT</th>
                                        <th>LOCATION</th>
                                        <th>ML RISK SCORE</th>
                                        <th>STATUS</th>
                                    </tr>
                                </thead>
                                <tbody id="workers-table-body">
                                    <!-- Populated via JS -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- Live Multi-Channel Sensor Telemetry Chart -->
                <div class="card shadow-sm">
                    <div class="card-header d-flex justify-content-between align-items-center">
                        <span><i class="fa-solid fa-chart-line me-2 text-primary"></i> Live Telemetry Waveforms (Target: WRK-VIT-40)</span>
                        <small class="text-secondary"><i class="fa-solid fa-clock me-1"></i> Polling 50Hz IMU / 1Hz Gas & Temp</small>
                    </div>
                    <div class="card-body">
                        <canvas id="telemetryChart" height="110"></canvas>
                    </div>
                </div>
            </div>

            <!-- Right Column: Map, Incident Alerts & Patent Architecture -->
            <div class="col-lg-4">
                <!-- GPS Map Tracking Card -->
                <div class="card shadow-sm">
                    <div class="card-header">
                        <i class="fa-solid fa-map-location-dot me-2 text-success"></i> Live GPS Geo-Tracking (Module 101)
                    </div>
                    <div class="card-body p-2">
                        <div id="map"></div>
                    </div>
                </div>

                <!-- Real-Time Alerts Feed -->
                <div class="card shadow-sm">
                    <div class="card-header d-flex justify-content-between align-items-center">
                        <span><i class="fa-solid fa-bell me-2 text-danger"></i> Emergency Incident Feed</span>
                        <span class="badge bg-danger" id="alert-count">1</span>
                    </div>
                    <div class="card-body p-3" style="max-height: 280px; overflow-y: auto;" id="alerts-container">
                        <!-- Populated via JS -->
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Patent Drawing & Specification Modal -->
    <div class="modal fade" id="patentModal" tabindex="-1" aria-labelledby="patentModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content bg-dark text-light border-secondary">
                <div class="modal-header border-secondary">
                    <h5 class="modal-title" id="patentModalLabel">
                        <i class="fa-solid fa-certificate text-warning me-2"></i> Official Patent Technical Drawings & Numerals (Figs 1–9)
                    </h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body text-center">
                    <img src="/figures/patent_drawings.jpg" alt="Patent Technical Drawings" class="img-fluid rounded border border-secondary mb-4 shadow">
                    <div class="table-responsive text-start">
                        <table class="table table-dark table-bordered">
                            <thead>
                                <tr class="table-secondary text-dark">
                                    <th>Numeral</th>
                                    <th>Subsystem Component</th>
                                    <th>Patent Specification & Function</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><strong>100</strong></td><td>Helmet Shell</td><td>High-impact thermoplastic structural protective casing.</td></tr>
                                <tr><td><strong>101</strong></td><td>GPS Module</td><td>Top crown-mounted geospatial receiver for search-and-rescue localization.</td></tr>
                                <tr><td><strong>102</strong></td><td>Temperature & Gas Sensor</td><td>Multi-modal sensor for heat stress, $CO, CH_4, H_2S, LPG$.</td></tr>
                                <tr><td><strong>103</strong></td><td>Buzzer & LED</td><td>Front-mounted 90dB acoustic buzzer and high-intensity alert LED.</td></tr>
                                <tr><td><strong>104</strong></td><td>Chin Strap</td><td>Ergonomic harness with integrated biometric photoplethysmography pulse sensor.</td></tr>
                                <tr><td><strong>105</strong></td><td>IMU (Accel/Gyro)</td><td>6-axis kinematic inertial measurement unit for fall/impact detection.</td></tr>
                                <tr><td><strong>106</strong></td><td>ESP32 Controller</td><td>Dual-core edge processor, ML inference engine, and Wi-Fi/LoRa transceiver.</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Leaflet & JS Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // Initialize Map
        const map = L.map('map').setView([18.4636, 73.8682], 16);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        let mapMarkers = {};

        // Initialize Chart.js
        const ctx = document.getElementById('telemetryChart').getContext('2d');
        const telemetryChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [
                    {
                        label: 'Risk Score (0-100)',
                        data: [],
                        borderColor: '#da3633',
                        backgroundColor: 'rgba(218, 54, 51, 0.1)',
                        fill: true,
                        tension: 0.3
                    },
                    {
                        label: 'Heart Rate (BPM)',
                        data: [],
                        borderColor: '#58a6ff',
                        tension: 0.3
                    },
                    {
                        label: 'Gas Level (PPM)',
                        data: [],
                        borderColor: '#d29922',
                        tension: 0.3
                    },
                    {
                        label: 'Temp (°C)',
                        data: [],
                        borderColor: '#238636',
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    x: { grid: { color: '#21262d' }, ticks: { color: '#8b949e' } },
                    y: { grid: { color: '#21262d' }, ticks: { color: '#8b949e' }, min: 0, max: 150 }
                },
                plugins: {
                    legend: { labels: { color: '#c9d1d9' } }
                }
            }
        });

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
                                    <div><i class="fa-solid fa-heart-pulse text-danger me-1"></i> <strong>${w.heart_rate}</strong> BPM</div>
                                    <small class="text-secondary">Accel: ${w.accel_mag}g | Jerk: ${w.jerk}g/s</small>
                                </td>
                                <td>
                                    <div><i class="fa-solid fa-temperature-three-quarters text-warning me-1"></i> <strong>${w.temperature}</strong>°C</div>
                                    <small class="text-secondary">Gas: ${w.gas_ppm} PPM</small>
                                </td>
                                <td>
                                    <i class="fa-solid fa-location-dot text-info me-1"></i> ${w.location_name}<br>
                                    <small class="text-secondary">${w.lat.toFixed(4)}, ${w.lng.toFixed(4)}</small>
                                </td>
                                <td style="min-width: 140px;">
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

                        // Update Map Marker
                        if (mapMarkers[id]) {
                            mapMarkers[id].setLatLng([w.lat, w.lng]);
                        } else {
                            mapMarkers[id] = L.marker([w.lat, w.lng])
                                .addTo(map)
                                .bindPopup(`<strong>${w.name}</strong><br>${id} - ${w.status}`);
                        }
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
                                <div class="small mt-1 text-light">${a.message}</div>
                                <small class="text-info mt-1 d-block"><i class="fa-solid fa-id-badge me-1"></i> Worker: ${a.worker_id}</small>
                            </div>
                        `;
                        alertsDiv.innerHTML += alertHtml;
                    });

                    // Update Chart for Target Worker
                    const target = data.workers['WRK-VIT-40'];
                    if (target) {
                        const nowTime = new Date().toLocaleTimeString();
                        if (telemetryChart.data.labels.length > 12) {
                            telemetryChart.data.labels.shift();
                            telemetryChart.data.datasets.forEach(d => d.data.shift());
                        }
                        telemetryChart.data.labels.push(nowTime);
                        telemetryChart.data.datasets[0].data.push(target.risk_score);
                        telemetryChart.data.datasets[1].data.push(target.heart_rate);
                        telemetryChart.data.datasets[2].data.push(target.gas_ppm);
                        telemetryChart.data.datasets[3].data.push(target.temperature);
                        telemetryChart.update();
                    }
                });
        }

        function triggerSim(action) {
            fetch('/api/simulate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: action })
            }).then(() => updateDashboard());
        }

        setInterval(updateDashboard, 2500);
        updateDashboard();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/figures/<path:filename>')
def serve_figures(filename):
    figures_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
    return send_from_directory(figures_dir, filename)

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
            "message": "High-g impact (5.4g) and high jerk detected on helmet shell. Worker motionless. Immediate dispatch required!",
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
    elif action == 'heat':
        workers_state["WRK-VIT-40"].update({
            "temperature": 43.5,
            "delta_temp": 2.1,
            "heart_rate": 148,
            "risk_score": 82,
            "risk_level": "High Risk",
            "status": "SEVERE_HEAT_STRESS",
            "last_update": datetime.now().strftime("%H:%M:%S")
        })
        alerts_log.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "worker_id": "WRK-VIT-40",
            "type": "CRITICAL HEAT STRESS & TACHYCARDIA",
            "message": "Core helmet temperature reached 43.5°C with worker heart rate at 148 BPM. High risk of thermal collapse!",
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
    app.run(host='0.0.0.0', port=5000, debug=False)
