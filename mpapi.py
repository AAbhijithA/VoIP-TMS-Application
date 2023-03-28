import streamlit as st
import requests
import json
import pandas as pd
st.title("Tracking location of user")
ip_address = st.text_input("Given IP address",value="Enter IP address")
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

