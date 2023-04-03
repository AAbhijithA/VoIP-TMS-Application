# VoIP/TMS Application
This is an application created by team **TANA** for the **TN Police Hackathon 2023** for the problem statement **VoIP/Telegram Message Scraping**.
The application uses Telegrams API in order to fetch and try phisihing the flagged individuals in groups or chats of the logged in user 
of the telegram application. The application has further functionalities in order to analyze the extracted data.
- - - -
### Functionalities
* **Telegram Message Extraction:** Lets us scrape the messages of multiple group chats using the telethon API and flag individuals using NLP via the textblob library in order to detect the levels of malicious content in text and flag individuals and we can send message to telegram offcials to retrive their ip address on request, the data is also additionally available to download for further investigation if needed.
* **Telegram Media Extraction:** Lets us scrape the media files like photos and audio files into a directory via telethon API in order to be used for later purposes *(Note: This functionality uses path so accordingly define where you need to save it otherwise it gets saved in your direcotry of this project).*
* **IP Geolocation Tracking:** Returns us the geolocation via IP-API to track any individuals location based on their IP-Address and returns more information to locate the cell tower location (latititude and longitude), ISP, etc. for tracking more details of flagged users.
* **VoIP Call Recordings to Text:** Converts mp3 recordings to text via OpenAI's Whisper API and do sentiment analysis on it and lets us understand if the call was malicious or not and we can get its subjectivity and polarity by NLP using textblob.
- - - -
### Setting up API's and Libraries
First we need to install all the requirements for running the project so we can either save these libraries in a virtual environment by downloading it with the command:
```
> pip install -r /path/to/requirements.txt
```
Or you can manually install each library using pip one by one via:
```
> pip install (library mentioned)
```
Make sure to make a telegram account before continuing to use the application and set up your Telegram API from the link below and replace all the api key and hash variables with the one assigned to you after creating your own telegram api: 

[Telegram API Site](https://core.telegram.org/)

Get your OpenAI Whisper API key from the OpenAI site by creating an account and signing up over here in the link below:

[OpenAI](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)

Make sure to input the mail via which you send emails of flagged individuals sendier id's and also the path functionality for media extraction of the path where you intend to save the media.
- - - -
### Setup for saving sessions
Since you wouldn't want to deal with logging into telegram and since its an asynchronous functionality and more tedious to integrate inot the application we can save a session string for automatic log in.

You can check telethons official documentation on this here: 
[Telethon Session Documentation](https://docs.telethon.dev/en/stable/concepts/sessions.html)

Our approach to this was first installing telethon
```
> pip install telethon
```
Now in a separate python file run the following code snippet:
```
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
```
copy the output in the terminal after logging into your telegram account which you created with your api key and hash and paste the following string outputted from the code above to every **session** variable in our code to automatically login to your telegram account.
```
session = '1aaNk8EX-YRfwoRsebUkugFvht6DUPi_Q25UOCzOAqzc...'
```
now just run the following snippet to run the application
```
> streamlit run About.py
```
You will be able to access all the functionalities of the application built after following all the steps given above. 
