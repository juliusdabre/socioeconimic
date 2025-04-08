
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the socioeconomic data
df = pd.read_excel("Socioeconomic.xlsx", sheet_name=0)
df.columns = df.columns.str.strip()

st.set_page_config(page_title="Socioeconomic Geo Map", layout="wide")
st.title("🌏 Socioeconomic Indicator Map")

# Map plot
fig = px.scatter_mapbox(
    df,
    lat="Long",  # Note: this is actually Longitude
    lon="Lat",   # Note: this is actually Latitude
    color="Socio-economic Ranking",
    hover_name="Suburb",
    hover_data={"State": True, "Socio-economic Ranking": True, "Lat": False, "Long": False},
    color_continuous_scale=[
        "#d73027", "#f46d43", "#fdae61", "#fee08b", "#d9ef8b",
        "#a6d96a", "#66bd63", "#1a9850", "#006837", "#004529"
    ],
    range_color=(1, 10),
    size_max=15,
    zoom=6,
    height=700,
    mapbox_style="open-street-map"
)

st.plotly_chart(fig, use_container_width=True)
