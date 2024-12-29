from pyrogram import Client
from Quiz.plugins.handlers import start_command, handle_photo, handle_text
from Quiz import app


# Handlers
app.add_handler(filters.command("start")(start_command))
app.add_handler(filters.photo(handle_photo))
app.add_handler(filters.text & ~filters.command(handle_text))
