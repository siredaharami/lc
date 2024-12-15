from pyrogram import Client 
from config import *
from .logging import LOGGER

# Initialize the bot client here
app = Client(
         name="Quiz-bot", 
         api_id=API_ID,
         api_hash=API_HASH,
         bot_token=BOT_TOKEN,
         plugins=dict(root="Quiz.plugins.tools")  # Ensure the plugins folder is structured correctly
)
)
