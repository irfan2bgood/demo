import matplotlib.pyplot as plt

flight_id = 5
f = df[df["flight_id"] == flight_id]

plt.figure(figsize=(14, 10))

# -------------------------
# 1. Anomaly score timeline
# -------------------------
plt.subplot(2, 2, 1)
plt.plot(f.index, f["anomaly_score"])
plt.axhline(f["anomaly_score"].quantile(ANOMALY_RATIO), linestyle="--")
plt.title(f"Flight {flight_id} – Anomaly Score")
plt.xlabel("Time")
plt.ylabel("Score")

# -------------------------
# 2. Engine temp anomalies
# -------------------------
plt.subplot(2, 2, 2)
plt.scatter(
    f.index,
    f["engine_temp"],
    c=f["anomaly"]
)
plt.title("Engine Temperature")
plt.xlabel("Time")
plt.ylabel("°C")

# -------------------------
# 3. Vibration distribution
# -------------------------
plt.subplot(2, 2, 3)
plt.hist(
    f["vibration"],
    bins=40
)
plt.title("Vibration Distribution")
plt.xlabel("Vibration")
plt.ylabel("Count")

# -------------------------
# 4. Anomalies per flight
# -------------------------
plt.subplot(2, 2, 4)
summary = df.groupby("flight_id")["anomaly"].sum()
plt.bar(summary.index, summary.values)
plt.title("Total Anomalies per Flight")
plt.xlabel("Flight ID")
plt.ylabel("Count")

plt.tight_layout()
plt.show()