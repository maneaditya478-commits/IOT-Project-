"""
Predictive Worker Safety Helmet - Supervisory Central Monitoring Dashboard
Flask Web Server providing real-time telemetry ingestion, interactive worker status,
predictive risk scoring gauges, alert dispatching, live waveform charts, and dynamic map tracking.
"""

from api.index import app

if __name__ == '__main__':
    print("\n" + "="*70)
    print(" 🚀 PREDICTIVE WORKER SAFETY HELMET - SUPERVISORY COMMAND CENTER")
    print(" Local Server: http://localhost:5000")
    print("="*70 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
