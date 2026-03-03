import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("📊 Global Population Dashboard")

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDNjYjc5N2EtNTJjZS00YmFiLTlhMWMtZTdjMGQ4MTQ1MDhmIiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D"


components.iframe(power_bi_url, height=750)

