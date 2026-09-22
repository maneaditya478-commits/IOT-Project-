# Predictive Worker Safety Helmet — IoT & Edge ML System

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/maneaditya478-commits/IOT-Project-)

## Project Overview
This project presents an **IoT and Machine Learning-Based Predictive Worker Safety Helmet with Real-Time Hazard Detection**, engineered to safeguard industrial and construction personnel from multi-modal environmental and physical hazards (falls, impacts, toxic gas accumulation, elevated heat stress, and cardiac anomalies).

---

## 🌐 Live Vercel Deployment Guide

### Option 1: Deploy via Vercel Web Dashboard (Easiest)
1. Go to [https://vercel.com](https://vercel.com) and log in with your GitHub account.
2. Click **"Add New..."** $\rightarrow$ **"Project"**.
3. Import your repository: **`maneaditya478-commits/IOT-Project-`**.
4. Leave all build settings as default (the included `vercel.json`, `api/index.py`, and `requirements.txt` configure everything automatically).
5. Click **"Deploy"**! Your live URL (e.g., `https://iot-project-xxx.vercel.app`) will be active in seconds.

### Option 2: Deploy via Vercel CLI
```bash
npm i -g vercel
vercel
```

---

## 📦 Deliverables in this Repository

| File | Description |
| :--- | :--- |
| **[Patent_Draft_Predictive_Worker_Safety_Helmet.docx](file:///d:/collage/MDM/course%20project/Patent_Draft_Predictive_Worker_Safety_Helmet.docx)** | **Official Word (.docx) Document** with standard formatting, claim structures, and embedded technical CAD drawings (Figs 1–9). |
| **[Patent_Draft_Predictive_Worker_Safety_Helmet.md](file:///d:/collage/MDM/course%20project/Patent_Draft_Predictive_Worker_Safety_Helmet.md)** | **Full 15-Section Patent Draft** adhering strictly to the official patent drafting template. |
| **[api/index.py](file:///d:/collage/MDM/course%20project/api/index.py)** | **Vercel Serverless Function & Live Dashboard** featuring Leaflet GPS mapping, real-time Chart.js telemetry waveforms, ML risk gauges, and interactive hazard simulation controls. |
| **[figures/patent_drawings.jpg](file:///d:/collage/MDM/course%20project/figures/patent_drawings.jpg)** | **Official Patent CAD Drawing Sheet** with Figs 1–9 and single-numeral callouts (100–106). |
| **[smart_helmet_firmware.ino](file:///d:/collage/MDM/course%20project/smart_helmet_firmware.ino)** | **ESP32 Edge Microcontroller Firmware** implementing multi-sensor sampling, MPU6050 fall detection, threshold checks, local buzzer/LED alarming, and LoRa/Wi-Fi telemetry dispatch. |
| **[ml_pipeline.py](file:///d:/collage/MDM/course%20project/ml_pipeline.py)** | **Machine Learning Training Pipeline** implementing feature extraction, Random Forest Risk Score regression ($0–100$), and tri-tier classification (Low/Medium/High Risk). |
| **[vercel.json](file:///d:/collage/MDM/course%20project/vercel.json)** & **[requirements.txt](file:///d:/collage/MDM/course%20project/requirements.txt)** | Vercel serverless deployment configuration and dependencies. |

---

## 🏗️ Hardware Architecture & Reference Numerals
* **`100`**: Helmet Shell (Protective outer thermoplastic casing)
* **`101`**: GPS Module (Top crown geospatial unit)
* **`102`**: Temperature & Gas Sensor (Multi-modal environmental module)
* **`103`**: Buzzer & LED (Audiovisual alarm & optical warning unit)
* **`104`**: Chin Strap (Harness with embedded PPG biometric pulse sensor)
* **`105`**: IMU (6-axis Accelerometer & Gyroscope kinematic sensor)
* **`106`**: ESP32 Controller (Main edge processing & Wi-Fi/LoRa unit)

---

## 💻 Local Execution

### 1. Run Machine Learning Pipeline
```powershell
python ml_pipeline.py
```

### 2. Launch Local Web Dashboard
```powershell
python dashboard_app.py
```
Open your browser at `http://localhost:5000` to interact with the command center, view worker telemetry, and test emergency fall/gas leak simulations.
