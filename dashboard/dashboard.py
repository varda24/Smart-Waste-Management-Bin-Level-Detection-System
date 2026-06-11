import streamlit as st
import pandas as pd

from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000, key="refresh")

st.set_page_config(
    page_title="Smart Waste Management Dashboard",
    layout="wide"
)

import os

csv_file = "data/bin_log.csv"

if not os.path.exists(csv_file):
    csv_file = "data/sample_bin_log.csv"

df = pd.read_csv(csv_file)


latest = df.iloc[-1]

fill = latest["FillPercent"]
status = latest["Status"]
alert = latest["Alert"]

st.title("🗑️ Smart Waste Management Dashboard")

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

if fill < 50:
    st.success("✅ Bin Status: EMPTY")

elif fill < 80:
    st.warning("⚠️ Bin Status: HALF FULL")

else:
    st.error("🚨 Collection Required")

st.subheader("📈 Fill Level Trend")

st.line_chart(df["FillPercent"])

st.subheader("📊 Fill Percentage Distribution")

chart_data = pd.DataFrame({
    "Category": ["Empty", "Filled"],
    "Value": [100-fill, fill]
})

st.bar_chart(
    chart_data.set_index("Category")
)

st.subheader("📋 Historical Data")

st.dataframe(df, use_container_width=True)