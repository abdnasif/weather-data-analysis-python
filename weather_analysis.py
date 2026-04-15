import pandas as pd
import matplotlib.pyplot as plt

# ══════════════════════════════════════════════════════════════════════════════
# 1. LOAD DATA
# ══════════════════════════════════════════════════════════════════════════════
weather  = pd.read_csv("weather.csv",  na_values="NULL")
stations = pd.read_csv("stations.csv", na_values="NULL")

print("=== 1. RAW DATA ===")
print(f"weather.csv  shape : {weather.shape}")
print(f"stations.csv shape : {stations.shape}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. CLEAN DATA
# ══════════════════════════════════════════════════════════════════════════════
print("\n=== 2. MISSING VALUES BEFORE CLEANING ===")
print(weather.isnull().sum())

# Parse date column
weather["Date"] = pd.to_datetime(weather["Date"])

# Numeric columns to fill
time_series_cols = [
    "Minimum Temperature",
    "Average Temperature",
    "Maximum Temperature",
    "relative humidity",
    "Average windspeed (Beaufort)",
    "Maximum windspeed (m/s)",
    "sunshine duration",
    "average cloud cover",
    "Rain",
    "average air preassure",
]

# Forward-fill then backward-fill per station (preserves time-series trend)
weather = weather.sort_values(["Stations_ID", "Date"])
weather[time_series_cols] = (
    weather.groupby("Stations_ID")[time_series_cols]
    .transform(lambda x: x.ffill().bfill())
)

# Global median fallback for any remaining NaNs
for col in time_series_cols:
    if weather[col].isnull().any():
        weather[col] = weather[col].fillna(weather[col].median())

# Clean stations (fill missing lat/lon/height with median if needed)
for col in ["geographic latitude", "geographic longitude", "height"]:
    if col in stations.columns and stations[col].isnull().any():
        stations[col] = stations[col].fillna(stations[col].median())

print("\n=== MISSING VALUES AFTER CLEANING ===")
print(weather.isnull().sum())

# Save cleaned files
weather.to_csv("weather_clean.csv",   index=False)
stations.to_csv("stations_clean.csv", index=False)
print("\nSaved: weather_clean.csv, stations_clean.csv")

# ══════════════════════════════════════════════════════════════════════════════
# 3. MERGE STATIONS WITH WEATHER
# ══════════════════════════════════════════════════════════════════════════════
merged = pd.merge(weather, stations, on="Stations_ID", how="left")

# Reorder columns: station info first, then weather measurements
station_cols = ["Stations_ID", "Location", "geographic latitude",
                "geographic longitude", "height", "Operator"]
weather_cols = ["Date", "Minimum Temperature", "Average Temperature",
                "Maximum Temperature", "relative humidity",
                "Average windspeed (Beaufort)", "Maximum windspeed (m/s)",
                "sunshine duration", "average cloud cover",
                "Rain", "average air preassure"]

merged = merged[station_cols + weather_cols]

print("\n=== 3. MERGED DATASET ===")
print(f"Shape          : {merged.shape}")
print(f"Unique stations: {merged['Stations_ID'].nunique()}")
print(f"Date range     : {merged['Date'].min().date()} to {merged['Date'].max().date()}")
print()
print(merged.head(10).to_string(index=False))

merged.to_csv("stations_weather_merged.csv", index=False)
print("\nSaved: stations_weather_merged.csv")

# ══════════════════════════════════════════════════════════════════════════════
# 4. PLOT — Monthly Average Temperature by Station
# ══════════════════════════════════════════════════════════════════════════════
stations_to_plot = ["Bremen", "Berlin-Tegel", "Augsburg", "Cuxhaven", "Brocken"]
sample = merged[merged["Location"].isin(stations_to_plot)].copy()

sample["Month"] = sample["Date"].dt.to_period("M").dt.to_timestamp()
monthly = (
    sample.groupby(["Month", "Location"])["Average Temperature"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(14, 6))

for location, group in monthly.groupby("Location"):
    ax.plot(group["Month"], group["Average Temperature"], label=location, linewidth=1.8)

ax.set_title("Monthly Average Temperature by Station (2016-2021)", fontsize=14, fontweight="bold")
ax.set_xlabel("Date")
ax.set_ylabel("Avg Temperature (C)")
ax.legend(title="Station", loc="upper right")
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("weather_plot.png", dpi=96)
print("\nPlot saved: weather_plot.png")
plt.show()
