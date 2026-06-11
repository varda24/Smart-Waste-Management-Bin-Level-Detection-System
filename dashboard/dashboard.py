import streamlit as st
import pandas as pd
import os

# Page Configuration
st.set_page_config(
    page_title="Smart Waste Management Dashboard",
    layout="wide"
)

st.title("🗑️ Smart Waste Management & Bin Level Detection System")

# Debug Information (remove later if desired)
st.write("Current Directory:", os.getcwd())

# Load Data
csv_file = "data/bin_log_backup.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)

else:
    st.error("Data file not found!")
    st.write("Files in current folder:", os.listdir("."))

    if os.path.exists("data"):
        st.write("Files inside data folder:", os.listdir("data"))

    df = pd.DataFrame({
        "Timestamp": ["No Data"],
        "Distance": [0],
        "FillPercent": [0],
        "Status": ["NO DATA"],
        "Alert": ["NO DATA"]
    })

# Latest Record
latest = df.iloc[-1]

distance = latest["Distance"]
fill = latest["FillPercent"]
status = latest["Status"]
alert = latest["Alert"]

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Distance (cm)", distance)

with col2:
    st.metric("Fill Percentage", f"{fill}%")

with col3:
    st.metric("Status", status)

with col4:
    st.metric("Alert", alert)

# Status Message
if fill < 50:
    st.success("✅ Bin Status: EMPTY")

elif fill < 80:
    st.warning("⚠️ Bin Status: HALF FULL")

else:
    st.error("🚨 COLLECTION REQUIRED")

# Trend Graph
st.subheader("📈 Fill Level Trend")

if len(df) > 1:
    st.line_chart(df["FillPercent"])
else:
    st.info("Not enough data for trend graph.")

# Data Table
st.subheader("📋 Historical Records")
st.dataframe(df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "Developed using ESP32, HC-SR04, Python, Streamlit and Wokwi Simulation"
)