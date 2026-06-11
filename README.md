# 🗑️ Smart Waste Management & Multi-Bin Monitoring System

## 🚀 Live Demo

🌐 **Live Dashboard:**
https://smart-waste-management-bin-level-detection-system-cgj8tintr3yx.streamlit.app/

---

# 📌 Overview

The Smart Waste Management & Multi-Bin Monitoring System is an IoT-based solution designed to monitor waste bin levels and optimize waste collection operations.

The project simulates smart waste bins using ESP32 and HC-SR04 Ultrasonic Sensor logic through Wokwi simulation and visualizes waste levels using a modern Streamlit dashboard.

The dashboard provides real-time monitoring of multiple bins, collection alerts, status analytics, and fill-level visualization.

---

# 🎯 Problem Statement

Traditional waste collection follows fixed schedules regardless of whether bins are full or empty.

This results in:

* Overflowing waste bins
* Unnecessary collection trips
* Increased fuel consumption
* Higher operational costs
* Poor resource utilization

This project provides a smart monitoring system that enables data-driven waste collection decisions.

---

# 🏙️ Smart City Use Cases

This solution can be used in:

* Smart Cities
* Municipal Corporations
* Airport Waste Management
* Railway Stations
* Shopping Malls
* Educational Campuses
* Corporate Parks
* Waste Collection Companies

---

# ⚙️ System Architecture

```text
HC-SR04 Sensor (Simulated)
            ↓
ESP32 Controller Logic
            ↓
Bin Fill Level Calculation
            ↓
Status Classification
            ↓
Data Logging (CSV)
            ↓
Streamlit Dashboard
            ↓
Analytics & Collection Alerts
```

---

# 🛠️ Technologies Used

## IoT & Hardware

* ESP32
* HC-SR04 Ultrasonic Sensor
* LED Indicators
* Buzzer
* Wokwi Simulator

## Software

* Python
* Pandas
* Streamlit
* Plotly
* Matplotlib

## Version Control

* Git
* GitHub

---

# ✨ Features

✅ Multi-Bin Monitoring

✅ Fill Percentage Calculation

✅ Bin Status Classification

✅ Smart Collection Alerts

✅ Interactive Dashboard

✅ Gauge Visualization

✅ Pie Chart Analytics

✅ Fill-Level Comparison

✅ Historical Data Tracking

✅ Streamlit Deployment

---

# 📊 Dashboard Features

## KPI Cards

* Total Bins
* Average Fill Percentage
* Bins Requiring Collection

## Visualizations

* Gauge Meters
* Fill-Level Comparison Chart
* Status Distribution Pie Chart
* Historical Monitoring Table

## Alerts

* EMPTY
* HALF FULL
* FULL
* COLLECTION REQUIRED

---

# 📂 Project Structure

```text
Smart-Waste-Management-Bin-Level-Detection-System/
│
├── arduino_code/
│   ├── sketch.ino
│   └── diagram.json
│
├── dashboard/
│   └── dashboard.py
│
├── python_simulation/
│   ├── bin_monitor.py
│   ├── plot_graph.py
│   ├── generate_report.py
│   └── multi_bin_generator.py
│
├── data/
│   ├── bin_log_backup.csv
│   └── multi_bin_data.csv
│
├── reports/
│   ├── fill_level_graph.png
│   └── waste_monitoring_report.pdf
│
├── images/
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📈 Bin Status Logic

| Fill Percentage | Status    |
| --------------- | --------- |
| 0 - 49%         | EMPTY     |
| 50 - 79%        | HALF FULL |
| 80 - 100%       | FULL      |

---

# 📊 Sample Dashboard Metrics

| Bin   | Fill Level | Status    |
| ----- | ---------- | --------- |
| Bin A | 35%        | EMPTY     |
| Bin B | 68%        | HALF FULL |
| Bin C | 92%        | FULL      |

---

# 🔔 Alert Logic

```text
EMPTY      → No Alert

HALF FULL  → Monitor

FULL       → Collection Required
```

---

# 📷 Screenshots

Add screenshots in the images folder and reference them here:

### Wokwi Circuit Diagram

![Circuit Diagram](images/circuit_diagram.png)

### Dashboard Overview

![Dashboard](images/dashboard.png)

### Analytics

![Analytics](images/analytics_graph.png)

---

# 🚀 How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

## Run Multi-Bin Generator

```bash
python python_simulation/multi_bin_generator.py
```

---

# 🎓 Learning Outcomes

This project demonstrates:

* IoT Fundamentals
* ESP32 Programming
* Sensor Integration
* Data Logging
* Dashboard Development
* Data Visualization
* Smart City Applications
* Git & GitHub Workflow
* Streamlit Deployment

---

# 🔮 Future Improvements

* MQTT Integration
* ThingSpeak Cloud Connectivity
* Node-RED Dashboard
* Mobile Application
* GPS-Based Collection Routing
* AI-Based Waste Collection Prediction

---

# 👨‍💻 Author

**Varda**

CSE (AIML) Student

IoT Course Project – Smart Waste Management & Multi-Bin Monitoring System
