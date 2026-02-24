import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# -------------------------
# 1. Load flight sensor data
# -------------------------
# Example CSV columns:
# airspeed, altitude, vertical_speed, engine_temp, vibration, fuel_flow

df = pd.read_csv("synthetic_flight_sensor_data.csv")

features = [
    "airspeed",
    "altitude",
    "vertical_speed",
    "engine_temp",
    "vibration",
    "fuel_flow"
]

X = df[features]

# -------------------------
# 2. Scale data
# -------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------
# 3. Train Isolation Forest
# -------------------------
iso_forest = IsolationForest(
    n_estimators=200,
    contamination=0.02,   # ~2% anomalies expected
    random_state=42
)

iso_forest.fit(X_scaled)

# -------------------------
# 4. Predict anomalies
# -------------------------
df["anomaly_score"] = iso_forest.decision_function(X_scaled)
df["anomaly"] = iso_forest.predict(X_scaled)

# Convert: -1 = anomaly, 1 = normal
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# -------------------------
# 5. View detected anomalies
# -------------------------
anomalies = df[df["anomaly"] == 1]
print(anomalies.head())