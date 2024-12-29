from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from Quiz.plugins.handlers import start_command, handle_photo, handle_text
from Quiz import app

# Register handlers
app.add_handler(MessageHandler(start_command, filters.command("start")))
app.add_handler(MessageHandler(handle_photo, filters.photo))
app.add_handler(MessageHandler(handle_text, filters.text & ~filters.command))
