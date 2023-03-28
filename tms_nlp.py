import streamlit as st
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import datetime
from datetime import timedelta
import pandas as pd
from textblob import TextBlob
import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
api_id = 27200016
api_hash = '8015e923aa186fc658122939fbf318de'
chats = []
s = st.text_input("Enter Group Chat Usernames with spacing: @",value="Enter usernames")
cht = str(s)
cht = cht.split()
for i in range(0,len(cht)):
    chats.append(cht[i])
d = st.number_input("Enter the number of days of messages to scrape: ",value=0)
df = pd.DataFrame()
if ((s!="Enter group username") and (d!=0)):
    #Scraping messages from chat
    session = '1BVtsOGQBu66fIFk8W4I3YMdncnh1W9lh3VG78-irlP-qV_VGatvfxBGKgKQgga7BZMiBCNbeoXijH0OMIzkt5LfDVnODO9WXfBCoVjm8O4xmxyc9WbWoGMr6CAqP8JNH8NVVWh6aKBPBeORG5ZHehlv4IHSRECkA1bYi7iJZm_qqR9vsuIWWwK4tGvKwtpDDs3hw4DIrsv_sOlHi0WKLue0XxzFf3ezOcayCvOdFXMZLukwkC1CwfLZUP2MlPeV9yCVNWbTQ2whQLrdErkpa9nskOVmUbtArGKJLLt2eCgbtzb-8yfRJPReAy12L_l538_YTDKM2DQWIFKlCO6mrrNo-fBTUfVc='
    client = TelegramClient(StringSession(session),api_id,api_hash)
    for chat in chats: 
        with TelegramClient(StringSession(session),api_id,api_hash) as client:
            for message in client.iter_messages(chat, offset_date=datetime.date.today()-timedelta(days=d),reverse=True):
                data = {"group": chat, "sender_id": message.sender_id, "sender_username": message.sender.username,"text": message.text, "date": message.date}
                tdf = pd.DataFrame(data,index=[1])
                df = df.append(tdf)
    #Filtering Messages with the help of NLP (Sentiment Polarity)
    df['text'] = df['text'].astype(str)
    sdf = pd.DataFrame()
    ndf = pd.DataFrame()
    for i in range(0,len(df)):
        sen = TextBlob(df.iloc[i,3]).sentiment.polarity
        sub = TextBlob(df.iloc[i,3]).sentiment.subjectivity
        if(sen<0.01):
            tdf = df.iloc[i]
            sent = {'Sentiment_Polarity':sen,'Sentiment_Subjectivity':sub}
            sdf = sdf.append(sent,ignore_index=True)
            ndf = ndf.append(tdf,ignore_index=True)
    ndf['Sentiment_Polarity'] = sdf['Sentiment_Polarity']
    ndf['Sentiment_Subjectivity'] = sdf['Sentiment_Subjectivity']
    st.write("Data Extracted")
    st.dataframe(df)
    l = []
    for tc in chats:
       a = df[df["group"]==tc]
       b = ndf[ndf["group"]==tc]
       alen = len(a)
       blen = len(b)
       alen = alen*4
       alen = alen//10
       if (blen > alen):
           l.append(tc)
    fg = pd.DataFrame(l,columns=['Group_name'])
    st.download_button(
        "Download csv file",
        df.to_csv(),
        file_name='original_csv.csv',
        mime = 'text/csv'
    )
    st.write("Data Filtered")
    st.dataframe(ndf)
    st.download_button(
        "Download filtered csv file",
        ndf.to_csv(),
        file_name='filtered_csv.csv',
        mime = 'text/csv'
    )
    st.write("Flagged groups")
    st.dataframe(fg)
    st.download_button(
        "Download flagged groups",
        fg.to_csv(),
        file_name='flagged_groups.csv',
        mime = 'text/csv'
    )