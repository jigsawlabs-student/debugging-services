import streamlit as st
import requests
url = 'api-deployment-service:5000/restaurants'
response = requests.get(url)
locations = response.json()

st.write("""
# My first app
Hello *world!*
""")

for location in locations['locations']:
    st.write(location[1])
