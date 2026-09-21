# Predictive Worker Safety Helmet — IoT & Edge ML System

## Project Overview
This project presents an **IoT and Machine Learning-Based Predictive Worker Safety Helmet with Real-Time Hazard Detection**, engineered to safeguard industrial and construction personnel from multi-modal environmental and physical hazards (falls, impacts, toxic gas accumulation, elevated heat stress, and cardiac anomalies).

---

## Deliverables in this Repository

| File | Description |
| :--- | :--- |
| **[Patent_Draft_Predictive_Worker_Safety_Helmet.md](file:///d:/collage/MDM/course%20project/Patent_Draft_Predictive_Worker_Safety_Helmet.md)** | **Complete Patent Draft Application** adhering strictly to the required 15-section official patent drafting format. |
| **[smart_helmet_firmware.ino](file:///d:/collage/MDM/course%20project/smart_helmet_firmware.ino)** | **ESP32 Edge Microcontroller Firmware** implementing multi-sensor sampling, MPU6050 fall detection, threshold checks, local buzzer/LED alarming, and LoRa/Wi-Fi telemetry dispatch. |
| **[ml_pipeline.py](file:///d:/collage/MDM/course%20project/ml_pipeline.py)** | **Machine Learning Training Pipeline** implementing feature extraction, Random Forest Risk Score regression ($0–100$), and tri-tier classification (Low/Medium/High Risk). |
| **[dashboard_app.py](file:///d:/collage/MDM/course%20project/dashboard_app.py)** | **Supervisory Command Center Dashboard (Flask)** with real-time telemetry tables, dynamic risk gauges, alert logs, and hazard event simulation. |
| **[synthetic_sensor_data.csv](file:///d:/collage/MDM/course%20project/synthetic_sensor_data.csv)** | Generated sensor dataset with multi-channel telemetry and ground-truth risk scores. |
| **[risk_prediction_model.pkl](file:///d:/collage/MDM/course%20project/risk_prediction_model.pkl)** | Trained and exported Machine Learning models. |

---

## 1. Official Patent Application Structure
The patent draft in `Patent_Draft_Predictive_Worker_Safety_Helmet.md` covers all 15 required sections:
1. **Applicant Information:** Vishwakarma Institute of Technology & Vishwakarma University.
2. **Inventor Details:** Prof. Vijaykumar Raghunath Ghule & Sail Sitaram Nagale.
3. **Title:** *IoT and Machine Learning-Based Predictive Worker Safety Helmet with Real-Time Hazard Detection* (14 words).
4. **Technical Field:** IoT, Embedded Systems, Edge Computing, Machine Learning, Occupational Safety.
5. **Prior Art:** In-depth comparative analysis highlighting deficiencies in passive headgear and static threshold sensors.
6. **Objectives of Invention:** 6 explicit technical and operational goals.
7. **Synopsis:** Structural breakdown, component bill of materials, and assembly flow.
8. **Brief Description of Drawings:** Common single numeral references (**100–111** and **200–205**).
9. **Detailed Description of Invention:** Rigorous mathematical formulations ($A_{mag}, J(t), \mu_{HR}, \Delta T/\Delta t$) and hardware integration details.
10. **Best Method of Performance:** Real-world step-by-step operating flow.
11. **Claims:** 8 formal patent claims (2 independent claims, 6 dependent claims).
12. **Inventive Step:** Clear justification of non-obviousness and technical superiority.
13. **Industrial Application:** Construction, mining, petrochemical plants, heavy manufacturing, and emergency response.
14. **Abstract:** Comprehensive single-paragraph summary.
15. **Drawings:** Clean architectural schematic and ML workflow diagrams with single-numeral callouts.

---

## 2. Running the Components

### Step 1: Run ML Pipeline
```powershell
python ml_pipeline.py
```

### Step 2: Launch Supervisory Web Dashboard
```powershell
python dashboard_app.py
```
Open your browser at `http://localhost:5000` to interact with the command center, view worker telemetry, and test emergency fall/gas leak simulations.
