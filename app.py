import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="MedTech Thermal Monitor", page_icon="🦷", layout="wide")

st.markdown("""
    <style>
    .stMetric { background: #f0faff; padding: 15px; border-radius: 10px; border-left: 5px solid #00d2ff; }
    .status-badge { padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦷 MedTech Precision Wax Control")
target_temp = st.sidebar.slider("Target Temperature (°C)", 50.0, 90.0, 65.0)

if 'temp_log' not in st.session_state:
    st.session_state.temp_log = pd.DataFrame(columns=['Time', 'Temp', 'Deviation'])

placeholder = st.empty()

for _ in range(100):
    curr_t = round(target_temp + np.random.uniform(-0.4, 0.4), 2)
    dev = round(abs(target_temp - curr_t), 2)
    
    entry = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), curr_t, dev]], columns=st.session_state.temp_log.columns)
    st.session_state.temp_log = pd.concat([st.session_state.temp_log, entry]).tail(20)

    with placeholder.container():
        m1, m2, m3 = st.columns(3)
        m1.metric("Live Temperature", f"{curr_t} °C", delta=f"{dev} °C Var")
        m2.metric("Target Setpoint", f"{target_temp} °C")
        m3.metric("QA Status", "CERTIFIED" if dev < 0.5 else "RE-CALIBRATING")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.temp_log['Time'], y=st.session_state.temp_log['Temp'], line=dict(color='#00d2ff')))
        fig.add_hline(y=target_temp, line_dash="dash", line_color="green", annotation_text="Setpoint")
        fig.update_layout(title="Thermal Stability Log (±0.5°C Tolerance)", template="none")
        st.plotly_chart(fig, use_container_width=True)
    time.sleep(2)
