# @title 2. Install All Dependencies
!pip install -q streamlit
!pip install -q streamlit-folium
!pip install -q streamlit-autorefresh
!pip install -q folium
!pip install -q plotly
!pip install -q pandas numpy
!pip install -q opencv-python pillow
!pip install -q geopy
!pip install -q pyngrok

# Verify installation
import streamlit as st
print(f"✅ Streamlit version: {st.__version__}")
print("✅ All packages installed successfully!")
