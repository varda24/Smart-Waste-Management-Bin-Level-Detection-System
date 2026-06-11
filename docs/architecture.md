# Smart Waste Management System Architecture

## Workflow

HC-SR04 Ultrasonic Sensor
↓
ESP32 Controller
↓
Distance Measurement
↓
Fill Percentage Calculation
↓
Status Classification
↓
Alert Generation
↓
CSV Logging
↓
Streamlit Dashboard
↓
PDF Report Generation

## Status Classification

| Fill Percentage | Status |
|---------------|---------|
| 0 - 49% | EMPTY |
| 50 - 79% | HALF FULL |
| 80 - 100% | FULL |

## Alert Logic

EMPTY → No Alert

HALF FULL → Monitor

FULL → Collection Required