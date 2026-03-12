import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("📊 Global INEQUALITY Dashboard")

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiMTMyNDk0ZjItODQwNS00N2E1LTg0NTQtYTg0YWU5MjVkZTQ3IiwidCI6IjgwOGNjODNlLWE1NDYtNDdlNy1hMDNmLTczYTFlYmJhMjRmMyIsImMiOjEwfQ%3D%3D"


components.iframe(power_bi_url, height=750)




