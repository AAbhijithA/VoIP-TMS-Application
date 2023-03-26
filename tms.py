from telethon.sync import TelegramClient
import datetime
from datetime import timedelta
import pandas as pd

api_id = #Enter your api-id
api_hash = #'Enter api-hash'
n = int(input("Enter the number of group chats to scrape: "))
chats = []
for i in range(0,n):
    s = str(input("Enter Group Chat Username: @"))
    chats.append(s)
d = int(input("Enter the number of days of messages to scrape: "))
df = pd.DataFrame()
client = TelegramClient(None,api_id,api_hash)
for chat in chats:
    with TelegramClient(None,api_id,api_hash) as client:
        for message in client.iter_messages(chat, offset_date=datetime.date.today()-timedelta(days=d),reverse=True):
            data = {"group": chat, "sender": message.sender_id,"text": message.text, "date": message.date}
            tdf = pd.DataFrame(data,index=[1])
            df = df.append(tdf)
print(df)

