from pyrogram import Client 
from config import *

# Initialize the bot client here
app = Client(
         "Quiz-bot", 
         api_id=API_ID,
         api_hash=API_HASH,
         bot_token=BOT_TOKEN
)
