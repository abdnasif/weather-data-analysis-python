# 🌦️ Weather Data Analysis with Python

## 📌 Overview
This project analyzes real-world weather data from the German Weather Service (DWD).  
The goal is to process, analyze, and visualize weather measurements from multiple stations over a selected time period.

The project demonstrates key concepts in Python programming, data analysis, and visualization.

---

## 🧠 Key Features

- 📥 Load and process CSV datasets using Pandas  
- 🔍 Detect and analyze missing data  
- 🏗️ Object-Oriented Programming (OOP) with custom classes  
- 🔗 Link weather measurements with station metadata  
- 📅 Filter data based on a user-defined time period  
- 📊 Compute statistical metrics (average values)  
- 📈 Visualize data using Matplotlib  
- 📍 Plot station locations on a map (scatter plot)  

---

## 🗂️ Dataset

The project uses two datasets:

1. **stations.csv**
   - Contains station metadata:
     - Station ID
     - Location
     - Latitude / Longitude
     - Height
     - Operator

2. **weather.csv**
   - Contains time-series weather data:
     - Date
     - Average Temperature
     - Average Windspeed (Beaufort)
     - Sunshine Duration

---

## ⚙️ Technologies Used

- Python 🐍
- Pandas 📊
- Matplotlib 📈
- Jupyter Notebook 📓

---

## 🧱 Project Structure
weather-data-analysis/
│
├── weather_module.py # Main module (classes & functions)
├── analysis.ipynb # Notebook for running and testing the project
├── stations.csv # Station dataset
├── weather.csv # Weather dataset
└── README.md # Project documentation


---

## 🧩 Object-Oriented Design

### 🔹 Station Class
Represents a weather station and stores:
- Station ID
- Location
- Coordinates
- Height
- Operator

### 🔹 WeatherStation Class (Inheritance)
Extends the Station class and adds:
- Weather data linked to each station
- Methods for analysis and visualization

---

## 📊 Data Analysis

The project calculates:

- 🌡️ Average Temperature  
- 💨 Average Windspeed  
- ☀️ Sunshine Duration  

These values are computed for each station within a selected time range.

---

## 📈 Visualizations

The project includes:

### 1️⃣ Station Locations (Scatter Plot)
- X-axis: Longitude  
- Y-axis: Latitude  
- Displays station IDs on the map  

### 2️⃣ Time-Series Plots (for selected station)
- Temperature vs Date  
- Windspeed vs Date  
- Sunshine Duration vs Date  

---
💡 What I Learned
Working with real-world datasets
Data cleaning and preprocessing
Using Pandas for filtering and analysis
Applying Object-Oriented Programming (OOP) in Python
Data visualization techniques with Matplotlib

---

🚀 Future Improvements
Interactive dashboards (Plotly / Dash)
Map visualization using Folium
Export results to reports
Performance optimization for large datasets


سششسيب
