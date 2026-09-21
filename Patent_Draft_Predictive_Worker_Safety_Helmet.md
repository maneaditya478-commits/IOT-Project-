# PATENT APPLICATION DRAFT

---

### 1. Full Name, Nationality and Address of Applicant(s):

| Full Name | Nationality | Address |
| :--- | :--- | :--- |
| **Vishwakarma Institute of Technology** | Indian | 666, Upper Indiranagar, Bibwewadi, Pune, Maharashtra, India – 411 037 |
| **Vishwakarma University** | Indian | Survey No 2, 3, 4, Kondhwa Main Rd, Laxmi Nagar, Betal Nagar, Kondhwa, Pune, Maharashtra, India – 411 048 |

---

### 2. Full Name (including middle name), Nationality, Address, Mail ID, and Phone Number of Inventor(s):

| Full Name (Including middle name) | Nationality | Address | Mail ID | Phone No. |
| :--- | :--- | :--- | :--- | :--- |
| **Prof. Vijaykumar Raghunath Ghule** | Indian | Department of Computer Science & Engineering (Data Science), Vishwakarma Institute of Technology, Pune, Maharashtra, India – 411 037 | vijaykumar.ghule@vit.edu | +91 8624046893 |
| **Sail Sitaram Nagale** | Indian | Department of Computer Science & Engineering (Data Science), Vishwakarma Institute of Technology, Pune, Maharashtra, India – 411 037 | sail.nagale@vit.edu | +91 [Contact Number] |

---

### Copy and paste clear soft copy of signatures of all inventors in the following table:

| Prof. Vijaykumar Raghunath Ghule | Sail Sitaram Nagale | [Inventor Name 3] | [Inventor Name 4] |
| :---: | :---: | :---: | :---: |
| *(Signature)* | *(Signature)* | *(Signature)* | *(Signature)* |
| **[Inventor Name 5]** | **[Inventor Name 6]** | **[Inventor Name 7]** | **[Inventor Name 8]** |
| *(Signature)* | *(Signature)* | *(Signature)* | *(Signature)* |

---

### 3. Title of the Invention:
**IOT AND MACHINE LEARNING-BASED PREDICTIVE WORKER SAFETY HELMET WITH REAL-TIME HAZARD DETECTION**

*(Word Count: 14 words)*

---

### 4. Technical Field of the Invention:
The present invention relates generally to industrial occupational safety, wearable embedded electronic systems, and edge computing. More specifically, the present invention relates to an Internet of Things (IoT) and Machine Learning (ML) integrated predictive smart helmet capable of multi-modal environmental sensing, real-time physiological parameter monitoring, kinematic fall and collision detection, localized risk classification, and wireless alert telemetry for construction and hazardous industrial environments.

---

### 5. Prior Art:
Conventional safety headgear used in industrial, construction, and mining facilities consists predominantly of passive thermoplastic or fiberglass shells engineered solely to cushion mechanical impact from falling debris. However, these traditional helmets cannot sense invisible hazards such as dangerous ambient toxic gases, prolonged extreme thermal exposure, or acute physiological distress in workers.

Recent advancements have led to basic electronic safety helmets that integrate single-variable sensors (e.g., a standalone gas detector or a simple tilt switch). However, existing smart helmet solutions exhibit significant technical limitations:
1. **Lack of Predictive Capability:** Existing devices operate on rigid, hardcoded instantaneous threshold triggers, which generate high rates of false alarms (e.g., momentary spikes in movement misidentified as falls) or fail to detect cumulative chronic hazards (e.g., gradual heat exhaustion or low-concentration toxic gas exposure).
2. **Absence of Multi-Sensor Fusion:** Conventional implementations fail to correlate physiological parameters (heart rate) with ambient variables (environmental temperature, hazardous gas concentrations) and kinematic vectors (6-axis acceleration and angular rate).
3. **High Latency & Cloud Dependency:** Many existing systems rely on constant cloud connectivity to process raw sensor feeds. When wireless signals deteriorate in tunnels, mines, or dense structural zones, monitoring fails.
4. **Lack of Integrated Precise Geo-Telemetry:** Existing systems frequently lack integrated spatial localization, complicating rescue operations when accidents occur across large-scale industrial plants.

The present invention overcomes these drawbacks by providing a self-contained, edge-intelligent wearable system that executes local feature extraction, multi-sensor data fusion, predictive risk scoring (0–100 scale), autonomous dual-tier audiovisual alarming, and hybrid long-range telemetry (Wi-Fi/LoRa) paired with GPS tracking.

---

### 6. Objective(s) of Invention:
The primary objectives of the present invention are:
1. To provide a comprehensive, non-intrusive smart safety helmet that continuously monitors environmental hazards, worker biometrics, and kinematic motion states in real time.
2. To provide an on-device edge processing mechanism combined with a trained machine learning predictive pipeline capable of computing a dynamic Safety Risk Score (0–100) and classifying conditions into Low, Medium, and High Risk tiers.
3. To accurately detect occupational emergencies including sudden falls, mechanical impacts, toxic gas accumulation, elevated core/helmet temperature, and abnormal cardiac variations before incidents become fatal.
4. To implement a dual-mode low-latency emergency response mechanism comprising instant localized audiovisual alarms (buzzer and high-luminescence LED) and automated wireless telemetry dispatch to a supervisory dashboard.
5. To incorporate geospatial coordinates via an onboard GPS receiver to enable immediate search and rescue dispatch in large-scale infrastructure environments.
6. To log continuous multi-modal time-series data to a secure centralized repository for retrospective accident analysis, predictive maintenance, and proactive workplace safety protocol optimization.

---

### 7. Synopsis:
The present invention is an IoT and Machine Learning-enabled Predictive Worker Safety Helmet designed to provide proactive and preventive occupational health and safety monitoring. The device is constructed by ergonomically embedding a low-power microcontroller unit (such as an ESP32 SoC), an ambient/internal temperature sensor, a toxic gas sensor, an optical photoplethysmography (PPG) heart rate sensor, a 6-axis Inertial Measurement Unit (IMU containing a 3-axis accelerometer and a 3-axis gyroscope), a Global Positioning System (GPS) module, an audiovisual alert module (piezoelectric buzzer and alert LED), and a hybrid wireless transceiver (Wi-Fi and LoRa) within a high-durability industrial safety helmet shell.

The microcontroller collects time-synchronized data streams from the multi-sensor array at scheduled intervals. An embedded preprocessing routine filters high-frequency noise and removes transmission artifacts before extracting statistical and kinematic features (e.g., acceleration vector magnitude, sudden jerk, rate of temperature increase, heart rate variability, and gas ppm concentration). An integrated machine learning model evaluates these extracted feature vectors against historical training profiles to produce a continuous numerical Risk Score (0 to 100). When the risk score breaches defined thresholds or when critical kinematic signatures (such as free-fall followed by non-responsive impact) occur, the system triggers local audiovisual feedback to alert the wearer and concurrently transmits emergency telemetry packets containing the worker ID, timestamp, biometric status, sensor anomalies, and exact GPS coordinates to a central monitoring cloud dashboard.

---

### 8. Brief Description of Drawings:

- **Figure 1** illustrates the architectural block diagram and electrical hardware configuration of the predictive worker safety helmet system according to the present invention.
- **Figure 2** illustrates the machine learning predictive risk assessment and emergency alert execution pipeline.

#### Reference Numerals Used in Drawings:
- **100:** Industrial Protective Helmet Shell
- **101:** Microcontroller and Edge Processing Unit (ESP32 SoC)
- **102:** Temperature Sensor Module
- **103:** Hazardous/Toxic Gas Sensor Module
- **104:** Biometric Photoplethysmography (PPG) Heart Rate Sensor
- **105:** 6-Axis Inertial Measurement Unit (IMU - Accelerometer and Gyroscope)
- **106:** Global Positioning System (GPS) Module
- **107:** Audiovisual Warning Unit (Piezoelectric Buzzer and Alert LED)
- **108:** Hybrid Wireless Telemetry Interface (Wi-Fi / LoRa Transceiver)
- **109:** Rechargeable Power Supply and Voltage Regulation Circuitry
- **110:** Cloud Server and Central Database Repository
- **111:** Supervisory IoT Monitoring Dashboard and Safety Officer Terminal
- **200:** Multi-Sensor Real-Time Data Acquisition Stage
- **201:** Edge Data Cleaning and Noise Filtering Stage
- **202:** Dynamic Feature Extraction Engine
- **203:** Machine Learning Predictive Risk Assessment Engine (Trained Model)
- **204:** Risk Scoring (0–100) and Tri-Level Classification Logic
- **205:** Dual-Action Local Warning and Cloud Telemetry Dispatch Module

---

### 9. Detailed Description of the Invention:

Referring to **Figure 1**, the present invention comprises an industrial protective helmet shell **(100)** fitted internally and externally with a distributed sensor network, a processing core, power management circuitry, and communication peripherals. The core computing hub is a microcontroller and edge processing unit **(101)**, preferably implemented using a dual-core 32-bit ESP32 microcontroller with integrated Wi-Fi and Bluetooth capabilities, interfaced with an extended LoRa transceiver.

The multi-modal sensing suite comprises:
1. **Temperature Sensor Module (102):** Strategically placed to measure both the micro-climate temperature inside the helmet shell **(100)** and ambient thermal conditions to detect worker heat exhaustion, hyperthermia, or fire exposure.
2. **Hazardous Gas Sensor Module (103):** Positioned on the exterior/visor perimeter of the helmet shell **(100)** to detect toxic and combustible gases including Carbon Monoxide (CO), Methane ($CH_4$), Hydrogen Sulfide ($H_2S$), and Liquefied Petroleum Gas (LPG).
3. **Biometric PPG Heart Rate Sensor (104):** Positioned on the inner forehead band or nape strap of the helmet shell **(100)** in direct skin contact to continuously measure pulse rate and blood volume changes.
4. **6-Axis Inertial Measurement Unit (105):** Rigidly mounted at the apex or center-of-mass of the helmet shell **(100)**, incorporating a 3-axis digital accelerometer and a 3-axis digital gyroscope (e.g., MPU6050) to measure dynamic acceleration vectors ($\vec{a} = [a_x, a_y, a_z]$) and rotational angular velocities ($\vec{\omega} = [\omega_x, \omega_y, \omega_z]$).
5. **GPS Module (106):** Interfaced with an omnidirectional ceramic patch antenna on top of the helmet shell **(100)** to calculate latitude, longitude, and elevation coordinates.

The system is powered by an onboard rechargeable lithium-polymer battery and power regulation unit **(109)** that incorporates overcharge, deep discharge, and short-circuit protection.

Referring to **Figure 2**, the operational sequence and predictive analytics pipeline are structured as follows:

#### A. Data Acquisition and Noise Filtering (200, 201)
Raw multi-sensor data is sampled at predetermined frequencies (e.g., IMU at 50 Hz, PPG at 20 Hz, Gas and Temperature at 1 Hz). The edge processor **(101)** applies moving-average smoothing, median filtering for spike suppression, and bandpass filtering to remove motion artifacts from the PPG heart rate stream.

#### B. Dynamic Feature Extraction (202)
From the conditioned sensor streams, the feature extraction engine derives:
- Total acceleration magnitude:
  $$A_{mag}(t) = \sqrt{a_x^2(t) + a_y^2(t) + a_z^2(t)}$$
- Dynamic jerk derivative:
  $$J(t) = \frac{d A_{mag}(t)}{dt}$$
- Moving average heart rate ($\mu_{HR}$) and heart rate variability (HRV) metrics.
- Rate of temperature elevation ($\Delta T / \Delta t$) and rolling peak temperature.
- Gas concentration moving average ($C_{gas}$) and instantaneous slope.

#### C. Machine Learning Predictive Risk Scoring (203, 204)
The extracted feature vector $\mathbf{X}(t) = [A_{mag}, J, \mu_{HR}, \Delta HR, T, \Delta T, C_{gas}]$ is fed into an embedded machine learning inference engine **(203)**. The model is pre-trained using supervised learning algorithms selected from Random Forest, Decision Trees, Gradient Boosted Classifiers, or Quantized Multi-Layer Perceptrons (MLP) trained on annotated datasets of normal worker activities, near-miss events, fall patterns, high heat stress, and gas exposure.

The model outputs a real-time normalized Safety Risk Score $R(t) \in [0, 100]$. The tri-level classification logic **(204)** maps the score as:
- **Low Risk ($0 \le R < 40$):** Normal operating status. Sensor streams are logged locally and transmitted at standard telemetry intervals (e.g., every 30 seconds).
- **Medium Risk ($40 \le R < 75$):** Pre-hazardous state (e.g., gradual heat buildup, elevated heart rate, moderate gas concentration). The helmet activates an intermittent alert via LED/buzzer **(107)** to caution the worker and flags an advisory notice on the supervisory dashboard **(111)**.
- **High Risk ($75 \le R \le 100$):** Critical emergency (e.g., sudden fall trajectory characterized by high jerk $J > J_{threshold}$ followed by static zero-velocity, acute gas burst $C_{gas} > C_{critical}$, or severe cardiac arrhythmia).

#### D. Dual-Action Alert & Telemetry Execution (205)
Upon high-risk classification:
1. The microcontroller instantly energizes the onboard piezoelectric buzzer and high-intensity LED **(107)** to warn the wearer and nearby colleagues.
2. The microcontroller encapsulates an emergency payload comprising `{Worker_ID, Timestamp, GPS_Lat, GPS_Long, HeartRate, Gas_PPM, Temp_C, Risk_Score, Incident_Type}` and broadcasts it over the wireless telemetry interface **(108)** using Wi-Fi (if local access point available) or fails over to long-range LoRa transmission.
3. The cloud server **(110)** receives the packet, writes it to the central database, and raises an urgent visual and audible alarm on the supervisory monitoring dashboard **(111)**, displaying the worker's exact location pin on an interactive map.

---

### 10. Best Method of Performance of the Invention:
The practical, exemplary implementation and operational workflow of the invention are performed as follows:

1. **System Initialization:** A worker equips the helmet **(100)** and powers on unit **(109)**. The microcontroller **(101)** executes a self-test diagnostic on all connected sensors **(102–106)**, establishes handshake with the nearest LoRa gateway / Wi-Fi mesh **(108)**, and synchronizes the worker's identification credentials.
2. **Continuous Edge Monitoring Cycle:** During routine industrial operations, the microcontroller executes continuous sensor polling loops. The 6-axis IMU **(105)** samples at 50 Hz, capturing all body kinematics. The heart rate sensor **(104)** continually samples cardiovascular pulse. The temperature **(102)** and gas **(103)** sensors sample ambient and interior parameters at 1-second intervals.
3. **Anomaly & Fall Detection Execution:** If a worker slips or loses balance from scaffolding, the IMU records a rapid acceleration drop (free fall) followed within 150 milliseconds by a high-g impact spike ($> 3.5g$) and subsequent lack of motion. The feature extraction engine detects this kinematic signature instantly.
4. **Predictive Heat Stress & Gas Inhalation Evaluation:** Concurrently, if the worker's heart rate climbs steadily above 130 bpm while internal helmet temperature exceeds 38°C and ambient gas sensor detects CO rising above 35 ppm, the ML model synthesizes these multi-sensor indicators, escalating the risk score from Low to High ($R \ge 85$) before the worker loses consciousness.
5. **Multi-Channel Emergency Response:** The microcontroller immediately drives the buzzer **(107)** at 90 dB pulse frequency and flashes the red LED. Simultaneously, an emergency telemetry packet containing latitude and longitude from the GPS module **(106)** is transmitted via LoRa to the base station **(110)**.
6. **Command Dashboard Dispatch:** The safety officer viewing the dashboard **(111)** receives an audio-visual emergency pop-up showing the worker's ID, medical status, environmental telemetry, and real-time map pin, enabling rescue personnel to locate and extract the worker within minutes.

---

### 11. CLAIMS:

**We Claim:**

1. An IoT and machine learning-enabled predictive worker safety helmet system comprising:
   - a protective helmet shell **(100)** configured to be worn by an industrial worker;
   - an environmental sensing unit including a temperature sensor **(102)** and a hazardous gas sensor **(103)** attached to said helmet shell;
   - a biometric sensing unit comprising a photoplethysmography (PPG) heart rate sensor **(104)** positioned to maintain contact with the worker's skin;
   - a kinematic sensing unit comprising a 6-axis inertial measurement unit (IMU) **(105)** including a 3-axis accelerometer and a 3-axis gyroscope;
   - a geospatial positioning unit comprising a global positioning system (GPS) module **(106)**;
   - an audiovisual warning unit **(107)** comprising an acoustic buzzer and a visual light emitting diode (LED);
   - a wireless communication transceiver **(108)** supporting dual-mode Wi-Fi and Long Range (LoRa) telemetry; and
   - a microcontroller and edge processing unit **(101)** communicatively coupled to said sensors, warning unit, and wireless transceiver, wherein said edge processing unit is configured to extract multi-modal feature vectors from real-time sensor data, compute a predictive safety risk score ($0$ to $100$) using an embedded machine learning model **(203)**, categorize said score into a plurality of risk levels **(204)**, and autonomously actuate said audiovisual warning unit **(107)** and transmit emergency telemetry packets to a supervisory dashboard **(111)** upon detection of a hazardous condition.

2. The system as claimed in claim 1, wherein said machine learning model **(203)** is trained on historical multi-modal industrial sensor data and evaluates an input feature vector comprising instantaneous acceleration magnitude, dynamic jerk derivative, moving average heart rate, rate of temperature increase, and toxic gas concentration to predict potential safety incidents before threshold failure.

3. The system as claimed in claim 1, wherein said edge processing unit **(101)** is configured with a tri-level risk classification logic comprising:
   - a Low Risk level ($0 \le R < 40$) signifying normal operational parameters;
   - a Medium Risk level ($40 \le R < 75$) triggering an advisory alert on said supervisory dashboard and intermittent local warning; and
   - a High Risk level ($75 \le R \le 100$) triggering continuous local acoustic and visual alarms and instantaneous transmission of emergency geospatial and physiological payloads.

4. The system as claimed in claim 1, wherein said kinematic sensing unit **(105)** executes a fall and collision detection routine configured to identify a free-fall acceleration signature followed by a high-g impact peak exceeding a defined acceleration threshold and a subsequent zero-motion window.

5. The system as claimed in claim 1, wherein said hazardous gas sensor **(103)** is configured to detect one or more toxic and flammable gases selected from the group consisting of Carbon Monoxide (CO), Methane ($CH_4$), Hydrogen Sulfide ($H_2S$), and Liquefied Petroleum Gas (LPG).

6. The system as claimed in claim 1, wherein said wireless communication transceiver **(108)** is configured with automated failover logic to transmit emergency packets over LoRa frequencies when local Wi-Fi network connectivity is unavailable.

7. The system as claimed in claim 1, wherein said emergency telemetry packet transmitted to said supervisory dashboard **(111)** comprises worker identification code, real-time GPS coordinates, time stamp, current heart rate, ambient gas concentration, helmet temperature, and current predictive risk score.

8. A computer-implemented method for predictive occupational safety monitoring using a smart helmet, comprising the steps of:
   - acquiring continuous time-synchronized data streams from a multi-sensor array comprising temperature, gas, heart rate, 6-axis IMU, and GPS sensors;
   - filtering raw sensor data to eliminate high-frequency noise and motion artifacts;
   - extracting dynamic temporal and kinematic features from the filtered sensor data;
   - executing an embedded machine learning predictive risk assessment algorithm on the extracted features to generate a normalized numerical risk score from $0$ to $100$;
   - comparing said risk score against defined safety classification thresholds;
   - energizing a local audiovisual alert unit on the helmet when the risk score exceeds a predetermined threshold; and
   - transmitting an emergency telemetry packet containing geospatial location and physiological metrics over a wireless interface to a remote monitoring dashboard for emergency response coordination.

---

### 12. Inventive Step of Your Invention:
The inventive step of the present invention resides in the technical convergence of:
1. **Multi-Modal Predictive Sensor Fusion vs. Static Thresholding:** Unlike conventional devices that trigger only after a catastrophic threshold breach occurs, the present invention extracts time-series dynamic features across biological, environmental, and kinematic channels simultaneously, enabling the machine learning model to detect escalating pre-incident conditions (e.g., onset of heat stroke under moderate gas exposure) well before worker incapacitation.
2. **Edge-Based Intelligence and Low Latency:** By embedding optimized feature extraction and ML inference directly on the low-power microcontroller **(101)**, the system eliminates mandatory cloud-inference round-trip delays, guaranteeing sub-second local alarm actuation even in radio-isolated tunnels or industrial basements.
3. **Dual-Mode Resilient Telemetry with Precise Geo-Tagging:** Incorporating automatic failover between high-bandwidth Wi-Fi and long-range, sub-GHz LoRa modulation ensures reliable communication of life-critical alerts combined with real-time GPS coordinates to emergency personnel across challenging industrial topographies.

---

### 13. Industrial Application:
The present invention has broad direct industrial application in:
1. **Building Construction and Civil Infrastructure:** Protecting workers from falls from heights, scaffolding accidents, crane collision zones, and structural collapses.
2. **Underground Mining and Tunneling:** Continuous monitoring of asphyxiating and combustible gases ($CO$, $CH_4$, $H_2S$), ambient oxygen depletion, and lone-worker entrapment.
3. **Petrochemical Refineries and Chemical Plants:** Immediate alert generation upon toxic vapor leaks, elevated pipeline thermal exposure, and worker collapse.
4. **Heavy Manufacturing, Metallurgy, and Foundries:** Monitoring heat stress index, blast furnace proximity risks, and intense mechanical impacts.
5. **Disaster Management and Firefighting Operations:** Real-time physiological tracking and location tracing of search-and-rescue personnel in dense hazardous zones.

---

### 14. Abstract:
An IoT and machine learning-enabled predictive worker safety helmet and method are disclosed for real-time hazard detection and proactive occupational safety monitoring. The smart helmet comprises an industrial helmet shell **(100)** integrating a microcontroller unit **(101)**, a temperature sensor **(102)**, a hazardous gas sensor **(103)**, a photoplethysmography heart rate sensor **(104)**, a 6-axis inertial measurement unit **(105)**, a GPS module **(106)**, an audiovisual alarm **(107)**, and a dual-mode wireless communication module **(108)**. The edge microcontroller continuously samples multi-modal sensor feeds, removes artifacts, extracts dynamic features, and executes an onboard machine learning model **(203)** to compute a real-time risk score ($0–100$) categorized into low, medium, and high risk levels. Upon detecting hazardous events—such as falls, toxic gas leaks, excessive thermal stress, or cardiac irregularities—the helmet instantly actuates local alarms and dispatches emergency telemetry packets containing exact GPS coordinates to a central supervisory dashboard **(111)** for rapid rescue intervention.

---

### 15. Drawings:

#### Figure 1: System Architecture and Hardware Block Diagram
```
+-----------------------------------------------------------------------------------+
|                        SMART HELMET ENCLOSURE (100)                               |
|                                                                                   |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|  | Temperature Sensor |  | Toxic Gas Sensor   |  | Heart Rate (PPG) Sensor     |  |
|  | (102)              |  | (103)              |  | (104)                       |  |
|  +---------+----------+  +---------+----------+  +--------------+--------------+  |
|            |                       |                            |                 |
|            +-----------------------+----------------------------+                 |
|                                    |                                              |
|  +--------------------+            v             +-----------------------------+  |
|  | 6-Axis IMU (MPU6050)| ---> [ MICROCONTROLLER ] <---| GPS Module (106)       |  |
|  | (105)              |     [ & EDGE PROCESSOR ] |                             |  |
|  +--------------------+     [ (ESP32 SoC) (101)] +-----------------------------+  |
|                                    |                                              |
|            +-----------------------+----------------------------+                 |
|            |                       |                            |                 |
|            v                       v                            v                 |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|  | Audiovisual Alert  |  | Hybrid Transceiver |  | Power Regulation & Battery  |  |
|  | (Buzzer & LED)(107)|  | (Wi-Fi/LoRa) (108) |  | (109)                       |  |
|  +--------------------+  +---------+----------+  +-----------------------------+  |
+------------------------------------|----------------------------------------------+
                                     | (Wireless Telemetry)
                                     v
                  +--------------------------------------+
                  | Cloud Server & Central Database (110)|
                  +------------------+-------------------+
                                     |
                                     v
                  +--------------------------------------+
                  | Supervisory Monitoring Dashboard     |
                  | & Safety Officer Terminal (111)      |
                  +--------------------------------------+
```

#### Figure 2: Machine Learning Predictive Risk Assessment Workflow
```
+-----------------------------------------------------------------------------------+
|                       DATA PROCESSING & PREDICTION PIPELINE                       |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|   +---------------------------------------------------------------------------+   |
|   | (200) Multi-Sensor Data Acquisition: Temperature, Gas, HR, IMU, GPS       |   |
|   +-------------------------------------+-------------------------------------+   |
|                                         |                                         |
|                                         v                                         |
|   +---------------------------------------------------------------------------+   |
|   | (201) Edge Preprocessing: Noise Filtering, Normalization, Spike Removal   |   |
|   +-------------------------------------+-------------------------------------+   |
|                                         |                                         |
|                                         v                                         |
|   +---------------------------------------------------------------------------+   |
|   | (202) Feature Extraction: Accel Magnitude, Jerk, HR Variability, Gas Rate |   |
|   +-------------------------------------+-------------------------------------+   |
|                                         |                                         |
|                                         v                                         |
|   +---------------------------------------------------------------------------+   |
|   | (203) ML Predictive Model: Decision Tree / Random Forest / Neural Network |   |
|   +-------------------------------------+-------------------------------------+   |
|                                         |                                         |
|                                         v                                         |
|   +---------------------------------------------------------------------------+   |
|   | (204) Risk Score Calculation (0-100) & Classification:                    |   |
|   |       • Low Risk (0-39)    --> Routine Periodic Log                       |   |
|   |       • Medium Risk (40-74)--> Precautionary Advisory                     |   |
|   |       • High Risk (75-100) --> Immediate Emergency Alarm                  |   |
|   +-------------------------------------+-------------------------------------+   |
|                                         |                                         |
|                                         v                                         |
|   +---------------------------------------------------------------------------+   |
|   | (205) Dual Action Dispatch: Local Buzzer/LED (107) + Remote Cloud/LoRa    |   |
|   |       Alert to Supervisory Dashboard (111) with GPS Coordinates           |   |
|   +---------------------------------------------------------------------------+   |
+-----------------------------------------------------------------------------------+
```
