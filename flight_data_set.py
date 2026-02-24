import numpy as np
import pandas as pd

np.random.seed(42)

# Parameters
num_flights = 20
points_per_flight = 200

data = []

for flight_id in range(1, num_flights + 1):
    
    time = np.arange(points_per_flight)
    
    # Normal flight behavior
    engine_temp = np.random.normal(650, 10, points_per_flight)
    vibration = np.random.normal(5, 0.5, points_per_flight)
    pressure = np.random.normal(30, 2, points_per_flight)
    fuel_flow = np.random.normal(2500, 100, points_per_flight)
    
    # Inject random anomalies (5 per flight)
    anomaly_indices = np.random.choice(points_per_flight, 5, replace=False)
    
    engine_temp[anomaly_indices] += np.random.normal(100, 20, 5)
    vibration[anomaly_indices] += np.random.normal(3, 1, 5)
    
    for i in range(points_per_flight):
        data.append([
            flight_id,
            time[i],
            engine_temp[i],
            vibration[i],
            pressure[i],
            fuel_flow[i]
        ])

df = pd.DataFrame(data, columns=[
    "flight_id",
    "time",
    "engine_temp",
    "vibration",
    "pressure",
    "fuel_flow"
])
# -------------------------
# Save
# -------------------------
df.to_csv("synthetic_flight_sensor_data.csv", index=False)

print("Dataset generated!")
print(df.head())
