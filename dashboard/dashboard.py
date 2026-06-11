import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Smart Waste Management Dashboard",
    page_icon="🗑️",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

st.title("🗑️ Smart Waste Management Dashboard")

# Simulated Multiple Bins
import os

csv_file = "data/multi_bin_data.csv"

if os.path.exists(csv_file):

    bins = pd.read_csv(csv_file)

else:

    bins = pd.DataFrame({
        "Bin": ["Bin A", "Bin B", "Bin C"],
        "FillPercent": [35, 68, 92]
    })

    def get_status(fill):

        if fill < 50:
            return "EMPTY"

        elif fill < 80:
            return "HALF FULL"

        return "FULL"

    bins["Status"] = bins["FillPercent"].apply(get_status)
# Status Logic

def get_status(fill):

    if fill < 50:
        return "EMPTY"

    elif fill < 80:
        return "HALF FULL"

    return "FULL"

bins["Status"] = bins["FillPercent"].apply(get_status)

# KPI Cards

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Bins",
        len(bins)
    )

with c2:
    st.metric(
        "Bins Requiring Attention",
        len(bins[bins["FillPercent"] >= 80])
    )

with c3:
    st.metric(
        "Average Fill %",
        round(bins["FillPercent"].mean(), 1)
    )

st.markdown("---")

# Individual Bin Gauges

st.subheader("📊 Bin Status Overview")

cols = st.columns(3)

for i, row in enumerate(bins.itertuples()):

    with cols[i]:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=row.FillPercent,
                title={"text": row.Bin},
                gauge={
                    "axis": {"range": [0, 100]}
                }
            )
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        st.write(
            f"Status: {row.Status}"
        )

# Fill Comparison

st.subheader("📈 Fill Level Comparison")

bar = px.bar(
    bins,
    x="Bin",
    y="FillPercent",
    text="FillPercent",
    title="Current Fill Level of All Bins"
)

st.plotly_chart(
    bar,
    use_container_width=True
)

# Distribution

st.subheader("📊 Status Distribution")

pie = px.pie(
    bins,
    names="Status",
    title="Waste Bin Status Distribution"
)

st.plotly_chart(
    pie,
    use_container_width=True
)

# Data Table

st.subheader("📋 Bin Monitoring Table")

st.dataframe(
    bins,
    use_container_width=True
)

# Alerts

critical = bins[bins["FillPercent"] >= 80]

if len(critical) > 0:

    st.error(
        f"🚨 {len(critical)} bin(s) require collection."
    )

else:

    st.success(
        "✅ All bins operating normally."
    )