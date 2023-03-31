import streamlit as st
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import MessageMediaDocument
import datetime
from datetime import timedelta
#import os
import asyncio
st.set_page_config(
    page_title="TANA"
)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown("<h1 style='text-align: center; color: white;'>Extracting media files in Telegram</h1>", unsafe_allow_html=True)
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

api_id = api_id
api_hash = 'API_HASH'
session = 'session'
client = TelegramClient(StringSession(session), api_id, api_hash)
cht = st.text_input("Enter the chat/group username: @",value="Enter")
chats = []
chats.append(cht)
d = st.number_input("Enter the number of days to scrape",value=0)
#path="Enter the file path to save the code to extract the final image/audio from and comment the current directory saving and uncomment the other with open loop"
if ((cht != "Enter") and (d != 0)):
    for chat in chats: 
        with TelegramClient(StringSession(session),api_id,api_hash) as client:
            for message in client.iter_messages(chat, offset_date=datetime.date.today()-timedelta(days=d),reverse=True):
                if message.media:
                    if isinstance(message.media, MessageMediaPhoto):
                        photo_id = message.media.photo.id
                        access_hash = message.media.photo.access_hash
                        photo = client.download_media(message.media)
                        #with open(os.path.join(path, f"{photo_id}.jpg"), "wb") as f:
                            #f.write(photo.encode('utf-8'))
                        with open(f"{photo_id}.jpg", "wb") as f:
                            f.write(photo.encode('utf-8'))
                    if isinstance(message.media, MessageMediaDocument):
                        if 'audio' in message.media.document.mime_type:
                            document_id = message.media.document.id
                            access_hash = message.media.document.access_hash
                            audio = client.download_media(message.media)
                            #with open(os.path.join(path, f"{document_id}.mp3"), "wb") as f:
                                #f.write(audio.encode('utf-8'))
                            with open(f"{document_id}.mp3", "wb") as f:
                                f.write(audio.encode('utf-8'))