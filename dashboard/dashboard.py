from streamlit_autorefresh import st_autorefresh
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
st_autorefresh(
    interval=5000,
    key="refresh"
)
st.set_page_config(
    page_title="Smart Waste Management Dashboard",
    page_icon="🗑️",
    layout="wide"
)

# Load Data
csv_file = "data/bin_log_backup.csv"

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    st.error("Data file not found")
    st.stop()

latest = df.iloc[-1]

fill = float(latest["FillPercent"])
distance = latest["Distance"]
status = latest["Status"]
alert = latest["Alert"]
timestamp = latest["Timestamp"]

# Title
st.title("🗑️ Smart Waste Management Dashboard")

st.markdown("---")

# KPI Cards
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Fill Level",
    f"{fill:.1f}%"
)

c2.metric(
    "Distance",
    f"{distance} cm"
)

c3.metric(
    "Status",
    status
)

c4.metric(
    "Total Readings",
    len(df)
)

# Alert Section

if fill >= 80:
    st.error("🚨 COLLECTION REQUIRED")

elif fill >= 50:
    st.warning("⚠️ BIN REACHING CAPACITY")

else:
    st.success("✅ BIN OPERATING NORMALLY")

st.markdown("---")

# Gauge + Pie
col1, col2 = st.columns(2)

with col1:

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fill,
        title={"text": "Current Fill Level (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"thickness": 0.3},
            "steps": [
                {"range": [0, 50]},
                {"range": [50, 80]},
                {"range": [80, 100]}
            ]
        }
    ))

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

with col2:

    counts = df["Status"].value_counts()

    pie = px.pie(
        values=counts.values,
        names=counts.index,
        title="Status Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# Trend Chart

st.subheader("📈 Fill Level Trend")

line = px.line(
    df,
    y="FillPercent",
    x="Timestamp",
    markers=True,
    title="Waste Fill Level Over Time"
)

st.plotly_chart(
    line,
    use_container_width=True
)

# Data Table

st.subheader("📋 Historical Records")

st.dataframe(
    df,
    use_container_width=True
)

# Footer

st.markdown("---")
st.write(
    f"Last Updated: {timestamp}"
)