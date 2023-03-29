import streamlit as st
from streamlit_lottie import st_lottie
import json
st.set_page_config(
    page_title="TANA",
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/lbcLMX9B6sTsGjUmS3/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.sidebar.title("Menu")
st.markdown("<h1 style='text-align: center; color: white;'>TN POLICE HACKATHON 2023</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>TANA</h1>", unsafe_allow_html=True)
c1,c2,c3 = st.columns(3)
st.write('''TANA is an application developed to aid law enforcement agencies track users of Telegram and VOIP. Malicious content sent over such networks is identified, scrapped and all the details of the offender including the geolocation can be retrieved. 
''')
st.markdown("<h3 style='text-align: center; color: white;'>SERVICES</h3>", unsafe_allow_html=True)


st.write('<div style="text-align:center">IP Address Tracker</div>', unsafe_allow_html=True)
st.write('<div style="text-align:center">Telegram Message Extraction</div>', unsafe_allow_html=True)
st.write('<div style="text-align:center">Telegram Media Extraction</div>', unsafe_allow_html=True)
st.write('<div style="text-align:center">IP Geolocation Tracking</div>', unsafe_allow_html=True)
st.write('<div style="text-align:center">VoIP Call Recordings to Text</div>', unsafe_allow_html=True)
