import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("📊 Global Population Dashboard")

power_bi_url = "https://adityagroup-my.sharepoint.com/:u:/g/personal/24p35a4208_acet_ac_in/IQCZMbekSQWRT6et8HsWAVbsAcAtNVpDCjLCid0x3KEwwGc?e=MyoSxr"


components.iframe(power_bi_url, height=750)
