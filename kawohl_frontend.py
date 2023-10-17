"""
# My first app
Here's our first attempt at using data to create a table:
# run command $ streamlit run kawohl_frontend.py 
"""

import streamlit as st
import pandas as pd
import requests
import json


api_data = requests.get("http://127.0.0.1:8000/items/?q=0&anotherelement=4").json()
dataframe_format = pd.read_json(api_data)
explore = dataframe_format.describe()
count = dataframe_format["Objekt_Anschriften"].value_counts() 
ordered = count.sort_values(ascending=False)


st.header("Kawohl")
st.write("Daten Exploration Objekt Anschriften liste")
st.dataframe(explore, use_container_width=True)
st.write("Der Anzahl der Objekt Anschriften von oben nach unten: ist: ")
st.dataframe(count, use_container_width=True)
st.json(api_data)
st.header("Problem Liste")































