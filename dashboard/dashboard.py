import streamlit as st
import pandas as pd
import os

# Page Config
st.set_page_config(
    page_title="Smart Waste Management Dashboard",
    layout="wide"
)

# Load Data Safely
if os.path.exists("data/bin_log.csv"):
    df = pd.read_csv("data/bin_log.csv")

elif os.path.exists("data/sample_bin_log.csv"):
    df = pd.read_csv("data/sample_bin_log.csv")

else:
    df = pd.DataFrame({
        "Timestamp": ["No Data"],
        "Distance": [0],
        "FillPercent": [0],
        "Status": ["NO DATA"],
        "Alert": ["NO DATA"]
    })

# Latest Record
latest = df.iloc[-1]

fill = latest["FillPercent"]
status = latest["Status"]
alert = latest["Alert"]

# Title
st.title("🗑️ Smart Waste Management Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Distance (cm)",
        latest["Distance"]
    )

with col2:
    st.metric(
        "Fill Percentage",
        f"{fill}%"
    )

with col3:
    st.metric(
        "Status",
        status
    )

with col4:
    st.metric(
        "Alert",
        alert
    )

# Status Alerts
if fill < 50:
    st.success("✅ Bin Status: EMPTY")

elif fill < 80:
    st.warning("⚠️ Bin Status: HALF FULL")

else:
    st.error("🚨 Collection Required")

# Trend Graph
st.subheader("📈 Fill Level Trend")

st.line_chart(df["FillPercent"])

# Distribution Chart
st.subheader("📊 Fill Percentage Distribution")

chart_data = pd.DataFrame({
    "Category": ["Empty Space", "Filled Space"],
    "Value": [100 - fill, fill]
})

st.bar_chart(
    chart_data.set_index("Category")
)

# Data Table
st.subheader("📋 Historical Data")

st.dataframe(
    df,
    use_container_width=True
)

# Footer
st.markdown("---")
st.markdown(
    "Smart Waste Management & Bin Level Detection System | ESP32 + HC-SR04 + Streamlit Dashboard"
)