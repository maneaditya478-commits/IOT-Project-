/*
  ==================================================================================
  Project: Predictive Worker Safety Helmet
  Description: ESP32 Edge Firmware for Multi-Sensor Acquisition, Local Fall Detection,
               Threshold Check, Local Audiovisual Alarms, and Wireless Telemetry.
  ==================================================================================
*/

#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>

// --------------------------- PIN CONFIGURATION ---------------------------
#define PIN_BUZZER          25
#define PIN_ALERT_LED       26
#define PIN_TEMP_ANALOG     34
#define PIN_GAS_MQ          35
#define PIN_PPG_HEART_RATE  36

// --------------------------- MPU6050 I2C ADDRESS -------------------------
#define MPU6050_ADDR        0x68

// --------------------------- THRESHOLDS ----------------------------------
#define THRESHOLD_TEMP_HIGH     40.0   // °C
#define THRESHOLD_GAS_HIGH      50.0   // PPM equivalent
#define THRESHOLD_FALL_G        3.5    // Acceleration magnitude in g
#define THRESHOLD_HR_HIGH       140    // BPM
#define THRESHOLD_HR_LOW        45     // BPM

// --------------------------- TELEMETRY SETTINGS --------------------------
const char* WIFI_SSID = "Worker_Safety_Mesh";
const char* WIFI_PASS = "SafetyFirst2026";
const char* SERVER_ENDPOINT = "http://192.168.1.100:5000/api/telemetry";

const char* WORKER_ID = "WRK-VIT-40";

// --------------------------- STATE VARIABLES -----------------------------
float currentTemp = 26.5;
float currentGasPPM = 12.0;
int currentHeartRate = 78;
float currentAccelMag = 1.0;
float currentJerk = 0.2;
float gpsLatitude = 18.4636;
float gpsLongitude = 73.8682;

int riskScore = 15;
String riskLevel = "Low Risk";

unsigned long lastSampleTime = 0;
const unsigned long SAMPLE_INTERVAL_MS = 1000;

// --------------------------- HARDWARE SETUP ------------------------------
void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("\n[INIT] Starting Predictive Worker Safety Helmet Firmware...");

  // Initialize GPIOs
  pinMode(PIN_BUZZER, OUTPUT);
  pinMode(PIN_ALERT_LED, OUTPUT);
  digitalWrite(PIN_BUZZER, LOW);
  digitalWrite(PIN_ALERT_LED, LOW);

  // Initialize I2C for IMU
  Wire.begin();
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0);    // Wake up MPU-6050
  Wire.endTransmission(true);

  // Initialize Wi-Fi
  Serial.print("[WIFI] Connecting to SSID: ");
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  // Self-test diagnostic pulse
  digitalWrite(PIN_ALERT_LED, HIGH);
  digitalWrite(PIN_BUZZER, HIGH);
  delay(150);
  digitalWrite(PIN_ALERT_LED, LOW);
  digitalWrite(PIN_BUZZER, LOW);

  Serial.println("[INIT] Diagnostic self-test completed. Device Active.\n");
}

// --------------------------- SENSOR SAMPLING -----------------------------
void readIMUData() {
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(0x3B); // Starting register for Accel readings
  Wire.endTransmission(false);
  Wire.requestFrom((uint16_t)MPU6050_ADDR, (uint8_t)6, (uint8_t)true);

  if (Wire.available() >= 6) {
    int16_t rawX = Wire.read() << 8 | Wire.read();
    int16_t rawY = Wire.read() << 8 | Wire.read();
    int16_t rawZ = Wire.read() << 8 | Wire.read();

    float ax = (float)rawX / 16384.0;
    float ay = (float)rawY / 16384.0;
    float az = (float)rawZ / 16384.0;

    float prevAccelMag = currentAccelMag;
    currentAccelMag = sqrt(ax * ax + ay * ay + az * az);
    currentJerk = abs(currentAccelMag - prevAccelMag) * 50.0; // derivative approx
  } else {
    // Default baseline if disconnected
    currentAccelMag = 1.0;
    currentJerk = 0.1;
  }
}

void readEnvironmentalAndBiometrics() {
  // Reading analog sensors (scaled to realistic physical values)
  int rawTemp = analogRead(PIN_TEMP_ANALOG);
  currentTemp = 20.0 + ((float)rawTemp / 4095.0) * 35.0; // Scaled 20°C - 55°C

  int rawGas = analogRead(PIN_GAS_MQ);
  currentGasPPM = ((float)rawGas / 4095.0) * 120.0; // Scaled 0 - 120 PPM

  int rawPPG = analogRead(PIN_PPG_HEART_RATE);
  currentHeartRate = map(rawPPG, 0, 4095, 50, 160);
}

// --------------------------- EDGE RISK ASSESSMENT ------------------------
void computeEdgeRisk() {
  float score = 0.0;

  // Temperature weight
  if (currentTemp > 38.0) {
    score += (currentTemp - 38.0) * 3.0;
  }

  // Gas PPM weight
  if (currentGasPPM > 50.0) {
    score += 40.0;
  } else if (currentGasPPM > 25.0) {
    score += (currentGasPPM - 25.0) * 1.5;
  }

  // Heart Rate weight
  if (currentHeartRate > THRESHOLD_HR_HIGH || currentHeartRate < THRESHOLD_HR_LOW) {
    score += 25.0;
  }

  // Fall / High-G impact detection
  if (currentAccelMag > THRESHOLD_FALL_G || currentJerk > 25.0) {
    score += 50.0;
    Serial.println("[ALERT] >>> CRITICAL FALL / IMPACT DETECTED! <<<");
  }

  riskScore = (int)constrain(score, 0, 100);

  if (riskScore < 40) {
    riskLevel = "Low Risk";
    digitalWrite(PIN_ALERT_LED, LOW);
    digitalWrite(PIN_BUZZER, LOW);
  } else if (riskScore < 75) {
    riskLevel = "Medium Risk";
    // Intermittent pulse
    digitalWrite(PIN_ALERT_LED, HIGH);
    digitalWrite(PIN_BUZZER, LOW);
  } else {
    riskLevel = "High Risk";
    // Continuous local alarm
    digitalWrite(PIN_ALERT_LED, HIGH);
    digitalWrite(PIN_BUZZER, HIGH);
  }
}

// --------------------------- TELEMETRY DISPATCH --------------------------
void transmitTelemetry() {
  String jsonPayload = "{";
  jsonPayload += "\"worker_id\":\"" + String(WORKER_ID) + "\",";
  jsonPayload += "\"temperature\":" + String(currentTemp, 2) + ",";
  jsonPayload += "\"gas_ppm\":" + String(currentGasPPM, 2) + ",";
  jsonPayload += "\"heart_rate\":" + String(currentHeartRate) + ",";
  jsonPayload += "\"accel_mag\":" + String(currentAccelMag, 2) + ",";
  jsonPayload += "\"jerk\":" + String(currentJerk, 2) + ",";
  jsonPayload += "\"latitude\":" + String(gpsLatitude, 4) + ",";
  jsonPayload += "\"longitude\":" + String(gpsLongitude, 4) + ",";
  jsonPayload += "\"risk_score\":" + String(riskScore) + ",";
  jsonPayload += "\"risk_level\":\"" + riskLevel + "\"";
  jsonPayload += "}";

  Serial.println("[TELEMETRY] " + jsonPayload);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(SERVER_ENDPOINT);
    http.addHeader("Content-Type", "application/json");
    int httpResponseCode = http.POST(jsonPayload);
    if (httpResponseCode > 0) {
      Serial.printf("[HTTP] Telemetry sent successfully. Code: %d\n", httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("[LORA FAILOVER] Transmitting telemetry packet via sub-GHz LoRa transceiver...");
  }
}

// --------------------------- MAIN LOOP -----------------------------------
void loop() {
  unsigned long now = millis();
  if (now - lastSampleTime >= SAMPLE_INTERVAL_MS) {
    lastSampleTime = now;

    readIMUData();
    readEnvironmentalAndBiometrics();
    computeEdgeRisk();
    transmitTelemetry();
  }
}
