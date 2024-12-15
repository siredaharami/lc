from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Quiz import app

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

quiz_data = [
    {
        "question": "What's the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct": 0  # Index of the correct option
    },
    {
        "question": "Who wrote '1984'?",
        "options": ["George Orwell", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"],
        "correct": 0
    },
]

# Quiz command handler
@app.on_message(filters.command("quiz"))
async def send_quiz(client, message):
    quiz = quiz_data[0]  # Select the first quiz
    question = quiz["question"]
    options = quiz["options"]
    correct_option_id = quiz["correct"]

    # Ensure question and options are within valid lengths
    if len(question) > 255:
        await message.reply("The question is too long!")
        return

    if any(len(option) > 100 for option in options):
        await message.reply("One of the options is too long!")
        return

    # Send a quiz poll to the group
    try:
        await message.reply_poll(
            question=question,
            options=options,
            type="quiz",
            correct_option_id=correct_option_id
        )
    except Exception as e:
        await message.reply(f"An error occurred: {e}")
