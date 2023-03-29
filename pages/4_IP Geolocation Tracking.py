import streamlit as st
import requests
import json
import pandas as pd
st.set_page_config(
    page_title="TANA"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.sidebar.title("Menu")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/xTiTnxpQ3ghPiB2Hp6/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.markdown("<h1 style='text-align: center; color: white;'>IP Geolocation Tracking</h1>", unsafe_allow_html=True)
ip_address = st.text_input("Give an IP address",value="Enter IP address")
if ip_address != "Enter IP address":
    response = requests.post("http://ip-api.com/batch",json=[
        {"query":ip_address}
        ]).json()
    for ip in response:
        location = {'lat':[ip['lat']],'lon':[ip['lon']]}
        df = pd.DataFrame(location)
        st.map(df)
        details = {'Country':[ip['country']],
                   'Region':[ip['regionName']],
                   'City':[ip['city']],
                   'Zip-Code':[ip['zip']],
                   'ISP':[ip['isp']],
                   'Org':[ip['org']],
                   'AS':[ip['as']],
                   'lat':[ip['lat']],
                   'lon':[ip['lon']]}
        st.title("\n\nOther Details")
        dedf = pd.DataFrame(details)
        st.dataframe(dedf)