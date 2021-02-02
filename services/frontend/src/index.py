import streamlit as st
import requests
url = 'http://api-deployment-service:5000/restaurants'
response = requests.get(url)
locations = response.json()


st.write("""
# My first app
Hello *world!*
""")


st.write(locations)

# for location in locations['locations']:
#     st.write(location[1])
