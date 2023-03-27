from telethon.sync import TelegramClient
import datetime
from datetime import timedelta
import pandas as pd
from textblob import TextBlob
api_id = #Enter API ID
api_hash = #'Enter API Hash'
n = int(input("Enter the number of group chats to scrape: "))
chats = []
for i in range(0,n):
    s = str(input("Enter Group Chat Username: @"))
    chats.append(s)
d = int(input("Enter the number of days of messages to scrape: "))
df = pd.DataFrame()
#Scraping Messages
client = TelegramClient(None,api_id,api_hash)
for chat in chats:
    with TelegramClient(None,api_id,api_hash) as client:
        for message in client.iter_messages(chat, offset_date=datetime.date.today()-timedelta(days=d),reverse=True):
            data = {"group": chat, "sender_id": message.sender_id,"text": message.text, "date": message.date}
            tdf = pd.DataFrame(data,index=[1])
            df = df.append(tdf)
#Filtering Messages with the help of NLP (Sentiment Polarity)
df['text'] = df['text'].astype(str)
sdf = pd.DataFrame()
ndf = pd.DataFrame()
for i in range(0,len(df)):
    sen = TextBlob(df.iloc[i,2]).sentiment.polarity
    sub = TextBlob(df.iloc[i,2]).sentiment.subjectivity
    if(sen<0):
        tdf = df.iloc[i]
        sent = {'Sentiment_Polarity':sen,'Sentiment_Subjectivity':sub}
        sdf = sdf.append(sent,ignore_index=True)
        ndf = ndf.append(tdf,ignore_index=True)
ndf['Sentiment_Polarity'] = sdf['Sentiment_Polarity']
ndf['Sentiment_Subjectivity'] = sdf['Sentiment_Subjectivity']
print(ndf)
#Storing the data as a csv file for later use
df.to_csv('data.csv')