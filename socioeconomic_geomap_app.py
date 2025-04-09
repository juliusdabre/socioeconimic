
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the socioeconomic data
df = pd.read_excel("Socioeconomic.xlsx", sheet_name=0)
df.columns = df.columns.str.strip()

st.set_page_config(page_title="Socioeconomic Geo Map", layout="wide")
st.title("🌏 Socioeconomic Indicator Map")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# State filter
state_options = sorted(df["State"].dropna().unique())
selected_states = st.sidebar.multiselect("Select State(s):", options=state_options, default=state_options)

# Ranking range filter
min_rank = int(df["Socio-economic Ranking"].min())
max_rank = int(df["Socio-economic Ranking"].max())
selected_rank_range = st.sidebar.slider(
    "Select Socio-economic Ranking Range:",
    min_value=min_rank,
    max_value=max_rank,
    value=(min_rank, max_rank)
)

# Filter dataframe
filtered_df = df[
    (df["State"].isin(selected_states)) &
    (df["Socio-economic Ranking"] >= selected_rank_range[0]) &
    (df["Socio-economic Ranking"] <= selected_rank_range[1])
]

# Map plot
fig = px.scatter_mapbox(
    filtered_df,
    lat="Long",  # Note: this is actually Longitude
    lon="Lat",   # Note: this is actually Latitude
    color="Socio-economic Ranking",
    hover_name="Suburb",
    hover_data={"State": True, "Socio-economic Ranking": True, "Lat": False, "Long": False},
    color_continuous_scale=[
        "#d73027", "#f46d43", "#fdae61", "#fee08b", "#d9ef8b",
        "#a6d96a", "#66bd63", "#1a9850", "#006837", "#004529"
    ],
    range_color=(min_rank, max_rank),
    size_max=15,
    zoom=6,
    height=700,
    mapbox_style="open-street-map"
)

st.plotly_chart(fig, use_container_width=True)
