import streamlit as st
import folium
from streamlit_folium import folium_static
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import random
from geopy.distance import distance

# Page config
st.set_page_config(
    page_title="Bharat Sagar Surveillance",
    page_icon="🇮🇳",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem 0;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #000080;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #666;
    }
    .alert-box {
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        color: white;
    }
    .critical { background-color: #dc3545; }
    .high { background-color: #fd7e14; }
    .medium { background-color: #ffc107; color: black; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1 style="color: #000080;">🇮🇳 BHARAT SAGAR SURVEILLANCE SYSTEM</h1>
    <h3 style="color: #000080;">Indian Navy - Maritime Domain Awareness</h3>
    <p style="color: #666;">Real-time vessel tracking with SAR-AIS fusion</p>
</div>
""", unsafe_allow_html=True)

# Generate data
def generate_data():
    vessels = []
    alerts = []

    # Indian locations
    locations = [
        {"name": "Mumbai", "lat": 18.95, "lon": 72.85},
        {"name": "Chennai", "lat": 13.08, "lon": 80.29},
        {"name": "Kolkata", "lat": 22.54, "lon": 88.30},
        {"name": "Kochi", "lat": 9.97, "lon": 76.27},
        {"name": "Visakhapatnam", "lat": 17.70, "lon": 83.30},
    ]

    vessel_types = ["Container Ship", "Oil Tanker", "Bulk Carrier", "Fishing Vessel",
                   "Naval Warship", "Passenger Ship"]

    for i in range(50):
        loc = random.choice(locations)
        vessel_type = random.choice(vessel_types)
        is_dark = random.random() < 0.1  # 10% dark vessels

        vessels.append({
            'name': f'Vessel-{i+1}',
            'type': vessel_type,
            'lat': loc['lat'] + random.uniform(-0.5, 0.5),
            'lon': loc['lon'] + random.uniform(-0.5, 0.5),
            'speed': round(random.uniform(5, 25), 1),
            'destination': random.choice(['Singapore', 'Colombo', 'Dubai']),
            'flag': random.choice(['India', 'Panama', 'Liberia']),
            'is_dark': is_dark,
            'risk': 'high' if is_dark else 'low'
        })

        if is_dark:
            alerts.append({
                'level': 'CRITICAL',
                'type': 'DARK VESSEL',
                'vessel': f'Vessel-{i+1}',
                'message': 'Vessel detected with AIS off',
                'action': 'Investigate immediately'
            })

    return vessels, alerts

vessels, alerts = generate_data()

# Top metrics
st.subheader("📊 Real-Time Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(vessels)}</div>
        <div class="metric-label">Total Vessels</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    dark_count = sum(1 for v in vessels if v['is_dark'])
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color: #dc3545;">{dark_count}</div>
        <div class="metric-label">Dark Vessels</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    naval_count = sum(1 for v in vessels if v['type'] == 'Naval Warship')
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color: #28a745;">{naval_count}</div>
        <div class="metric-label">Naval Ships</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color: #fd7e14;">{len(alerts)}</div>
        <div class="metric-label">Active Alerts</div>
    </div>
    """, unsafe_allow_html=True)

# Performance metrics
st.subheader("🎯 System Performance")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">94.5%</div>
        <div class="metric-label">SAR Accuracy</div>
        <div style="background: #e0e0e0; height: 5px; border-radius: 5px; margin-top: 5px;">
            <div style="width: 94.5%; background: #000080; height: 5px; border-radius: 5px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">92.3%</div>
        <div class="metric-label">AIS Reliability</div>
        <div style="background: #e0e0e0; height: 5px; border-radius: 5px; margin-top: 5px;">
            <div style="width: 92.3%; background: #000080; height: 5px; border-radius: 5px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">96.8%</div>
        <div class="metric-label">Fusion Accuracy</div>
        <div style="background: #e0e0e0; height: 5px; border-radius: 5px; margin-top: 5px;">
            <div style="width: 96.8%; background: #000080; height: 5px; border-radius: 5px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Map
st.subheader("🗺️ Live Maritime Picture")
m = folium.Map(location=[15.0, 80.0], zoom_start=5)

# Add Indian EEZ
folium.GeoJson(
    {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[65.0, 6.0], [65.0, 28.0], [92.0, 28.0], [92.0, 6.0], [65.0, 6.0]]]
        }
    },
    style_function=lambda x: {'fillColor': '#000080', 'color': '#000080', 'weight': 1, 'fillOpacity': 0.1}
).add_to(m)

# Add vessels
for v in vessels:
    color = 'red' if v['is_dark'] else 'green'
    folium.CircleMarker(
        location=[v['lat'], v['lon']],
        radius=5,
        color=color,
        fill=True,
        popup=f"{v['name']}<br>{v['type']}<br>Speed: {v['speed']} kts"
    ).add_to(m)

folium_static(m, width=1000, height=500)

# Alerts
if alerts:
    st.subheader("🚨 Active Alerts")
    for alert in alerts[:5]:
        alert_class = "critical" if alert['level'] == 'CRITICAL' else "high" if alert['level'] == 'HIGH' else "medium"
        st.markdown(f"""
        <div class="alert-box {alert_class}">
            <strong>{alert['level']}: {alert['type']}</strong><br>
            {alert['message']} - {alert['action']}
        </div>
        """, unsafe_allow_html=True)

# Analytics
st.subheader("📈 Analytics")
col1, col2 = st.columns(2)

with col1:
    # Vessel types
    type_counts = {}
    for v in vessels:
        type_counts[v['type']] = type_counts.get(v['type'], 0) + 1

    fig = px.pie(
        values=list(type_counts.values()),
        names=list(type_counts.keys()),
        title="Vessel Types"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Speed distribution
    speeds = [v['speed'] for v in vessels]
    fig = px.histogram(
        x=speeds,
        nbins=10,
        title="Speed Distribution",
        labels={'x': 'Speed (knots)'}
    )
    st.plotly_chart(fig, use_container_width=True)

# Vessel table
st.subheader("📋 Vessel List")
df = pd.DataFrame(vessels)
st.dataframe(
    df[['name', 'type', 'speed', 'destination', 'flag', 'is_dark']],
    use_container_width=True,
    hide_index=True
)

# Footer
st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST")
st.caption("🇮🇳 Bharat Sagar Surveillance System | For Indian Navy Use Only")
