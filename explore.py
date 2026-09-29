import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Crop_Recommendation.csv")

# Clean the data
print("Rows before cleaning:", len(df))
df = df.drop_duplicates()
df = df.dropna()
print("Rows after cleaning:", len(df))

# Chart 1: average rainfall by crop
avg_rain = df.groupby("Crop")["Rainfall"].mean().sort_values()
avg_rain.plot(kind="barh", figsize=(8, 10))
plt.title("Average Rainfall by Crop")
plt.xlabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("rainfall_by_crop.png")
plt.close()

# Chart 2: temperature vs humidity
plt.figure(figsize=(8, 6))
plt.scatter(df["Temperature"], df["Humidity"], alpha=0.5)
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("temp_vs_humidity.png")
plt.close()

# Chart 3: soil pH distribution
plt.figure(figsize=(8, 6))
plt.hist(df["pH_Value"], bins=20)
plt.title("Soil pH Distribution")
plt.xlabel("pH")
plt.ylabel("Count")
plt.savefig("ph_distribution.png")
plt.close()

print("Done! Check your folder for 3 PNG charts.")