import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
# Google verification meta tag
components.html(
    """
    <meta name="google-site-verification" content="-SFsJYFzgpk9IHnfjY5-D1gatuCSUZnvIwWv4Xhazbs" />
    """,
    height=0,
)

st.title("📊 Global Population Dashboard")

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZDNjYjc5N2EtNTJjZS00YmFiLTlhMWMtZTdjMGQ4MTQ1MDhmIiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D"


components.iframe(power_bi_url, height=750)


