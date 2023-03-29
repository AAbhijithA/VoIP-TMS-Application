import streamlit as st
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import telegram
import datetime
from datetime import timedelta
import pandas as pd
from textblob import TextBlob
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
st.markdown("<h1 style='text-align: center; color: white;'>Extracting Messages in Telegram</h1>", unsafe_allow_html=True)
st.sidebar.title("Menu")


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/3oFzmrqRPhYnFg9oGs/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def email(s_id):
    # set up the email message
    sender_email = 'sender_email'
    receiver_email = 'receiver_email' #replace it with telegrams mail address
    password = 'PASSWORD'
    subject = "Subject: Request to telegram"
    message = "Message to telegram urgent! please let us get the IP address of "+str(s_id)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # send the email
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
def link():
    bot = telegram.Bot(token='BOT_TOKEN')
    sender_id = 'SENDER_ID'  # replace with the actual sender ID
    message = 'Message'  # replace with your message
    bot.send_message(chat_id=sender_id, text=message)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
api_id = api_id
api_hash = 'API_HASH'
chats = []
s = st.text_input("Enter Group/Chat Usernames with spacing: @",value="Enter usernames")
cht = str(s)
cht = cht.split()
for i in range(0,len(cht)):
    chats.append(cht[i])
d = st.number_input("Enter the number of days of messages to scrape: ",value=0)
df = pd.DataFrame()
if ((s!="Enter group username") and (d!=0)):
    #Scraping messages from chat
    session = 'Session'
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
    t_df = pd.DataFrame()
    t_df['sender_id'] = ndf['sender_id']
    t_df['sender_username'] = ndf['sender_username']
    t_df['S.No'] = range(1,len(t_df)+1)
    st.write("Flagged individuals")
    st.dataframe(t_df)
    st.download_button(
        "Download flagged individuals file",
        t_df.to_csv(),
        file_name='flagged.csv',
        mime = 'text/csv'
    )
    s_no = st.number_input("Enter the serial no. of sender: ",value=1)
    s_id = t_df.loc[t_df['S.No'] == s_no, 'sender_id'].iloc[0]

    if st.button('Send Email'):
        email(s_id)
        st.success('Email sent!')

    elif st.button('Send Link'):
        link()
        st.success('Link sent!')
