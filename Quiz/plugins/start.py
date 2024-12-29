from pyrogram import Client, filters
from Quiz.plugins.handlers import handle_photo, handle_text, handle_callback_query
from Quiz import app

users_data = {}

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the Logo Maker Bot!\nPlease send me an image.")

app.add_handler(handle_photo)
app.add_handler(handle_text)
app.add_handler(handle_callback_query)
