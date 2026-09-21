"""
Predictive Worker Safety Helmet - Machine Learning Risk Prediction Pipeline
This script simulates multi-modal industrial sensor streams, trains predictive models
(Random Forest & Gradient Boosting) to compute continuous Safety Risk Scores (0-100) 
and tri-tier classifications (Low, Medium, High Risk), and exports the model.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import classification_report, mean_squared_error, r2_score
import joblib
import os

def generate_synthetic_dataset(num_samples=5000, random_seed=42):
    np.random.seed(random_seed)
    
    # 1. Temperature (°C): Normal 22-34, Heat stress > 38, Critical > 45
    temp = np.random.normal(loc=28.0, scale=5.0, size=num_samples)
    temp = np.clip(temp, 15.0, 55.0)
    
    # Rate of temperature change (°C/min)
    delta_temp = np.random.normal(loc=0.1, scale=0.5, size=num_samples)
    
    # 2. Hazardous Gas (PPM) - CO / Methane: Normal < 25, Hazardous 25-50, Dangerous > 50
    gas_ppm = np.random.exponential(scale=12.0, size=num_samples)
    gas_ppm = np.clip(gas_ppm, 0.0, 150.0)
    
    # 3. Heart Rate (BPM): Normal 60-100, Elevated/Stress 100-140, Critical > 140 or < 45
    heart_rate = np.random.normal(loc=80.0, scale=18.0, size=num_samples)
    heart_rate = np.clip(heart_rate, 40.0, 180.0)
    
    # 4. Acceleration Magnitude (g): Normal walking 0.8-1.4, Running 1.4-2.2, Fall/Impact > 3.5
    accel_mag = np.random.normal(loc=1.0, scale=0.25, size=num_samples)
    # Inject fall/impact anomalies into 5% of samples
    fall_indices = np.random.choice(num_samples, size=int(num_samples * 0.06), replace=False)
    accel_mag[fall_indices] = np.random.uniform(3.5, 8.0, size=len(fall_indices))
    
    # 5. Jerk (g/s): Rate of change of acceleration
    jerk = np.random.normal(loc=0.5, scale=0.8, size=num_samples)
    jerk[fall_indices] = np.random.uniform(15.0, 60.0, size=len(fall_indices))
    
    # Calculate Ground Truth Risk Score (0-100) based on weighted non-linear hazard functions
    risk_scores = np.zeros(num_samples)
    for i in range(num_samples):
        score = 0.0
        
        # Thermal hazard contribution
        if temp[i] > 38.0:
            score += min(30.0, (temp[i] - 38.0) * 2.5 + delta_temp[i] * 5.0)
        elif temp[i] > 32.0:
            score += (temp[i] - 32.0) * 1.5
            
        # Gas hazard contribution
        if gas_ppm[i] > 50.0:
            score += 35.0 + min(15.0, (gas_ppm[i] - 50.0) * 0.3)
        elif gas_ppm[i] > 25.0:
            score += (gas_ppm[i] - 25.0) * 1.4
            
        # Cardiovascular stress contribution
        if heart_rate[i] > 130.0:
            score += min(25.0, (heart_rate[i] - 130.0) * 0.8)
        elif heart_rate[i] < 50.0:
            score += 20.0
            
        # Kinematic impact / fall contribution
        if accel_mag[i] > 3.5 or jerk[i] > 20.0:
            score += min(45.0, (accel_mag[i] - 1.0) * 8.0 + jerk[i] * 0.4)
            
        # Add slight natural variance and clamp between 0 and 100
        score += np.random.normal(0, 2.0)
        risk_scores[i] = np.clip(score, 0.0, 100.0)
        
    # Classify into 3 Tiers
    risk_classes = []
    for s in risk_scores:
        if s < 40.0:
            risk_classes.append("Low Risk")
        elif s < 75.0:
            risk_classes.append("Medium Risk")
        else:
            risk_classes.append("High Risk")
            
    df = pd.DataFrame({
        'temperature': np.round(temp, 2),
        'delta_temp': np.round(delta_temp, 2),
        'gas_ppm': np.round(gas_ppm, 2),
        'heart_rate': np.round(heart_rate, 1),
        'accel_magnitude': np.round(accel_mag, 2),
        'jerk': np.round(jerk, 2),
        'risk_score': np.round(risk_scores, 2),
        'risk_level': risk_classes
    })
    
    return df

def train_models():
    print("Generating synthetic sensor training dataset...")
    df = generate_synthetic_dataset(num_samples=6000)
    
    features = ['temperature', 'delta_temp', 'gas_ppm', 'heart_rate', 'accel_magnitude', 'jerk']
    X = df[features]
    y_reg = df['risk_score']
    y_clf = df['risk_level']
    
    X_train, X_test, y_reg_train, y_reg_test, y_clf_train, y_clf_test = train_test_split(
        X, y_reg, y_clf, test_size=0.2, random_state=42
    )
    
    print("Training Random Forest Regressor for continuous Risk Score (0-100)...")
    regressor = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42)
    regressor.fit(X_train, y_reg_train)
    
    y_pred_reg = regressor.predict(X_test)
    mse = mean_squared_error(y_reg_test, y_pred_reg)
    r2 = r2_score(y_reg_test, y_pred_reg)
    print(f"Regression Evaluation -> MSE: {mse:.4f}, R² Score: {r2:.4f}")
    
    print("\nTraining Random Forest Classifier for Tri-Tier Risk Level...")
    classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    classifier.fit(X_train, y_clf_train)
    
    y_pred_clf = classifier.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_clf_test, y_pred_clf))
    
    # Feature importances
    importances = pd.Series(regressor.feature_importances_, index=features).sort_values(ascending=False)
    print("\nFeature Importances:")
    print(importances)
    
    # Save artifacts
    output_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(output_dir, 'synthetic_sensor_data.csv')
    model_path = os.path.join(output_dir, 'risk_prediction_model.pkl')
    
    df.to_csv(data_path, index=False)
    joblib.dump({
        'regressor': regressor,
        'classifier': classifier,
        'features': features
    }, model_path)
    
    print(f"\nSaved dataset to: {data_path}")
    print(f"Saved trained models to: {model_path}")
    return regressor, classifier

if __name__ == '__main__':
    train_models()
