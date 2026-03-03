import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("📊 Global Population Dashboard")

power_bi_url = "PASTE_YOUR_EMBED_LINK_HERE"

components.iframe(power_bi_url, height=750)