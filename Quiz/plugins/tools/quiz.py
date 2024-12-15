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
    quiz = quiz_data[0]  # You can rotate this to send different quizzes
    question = quiz["question"]
    options = quiz["options"]

    # Send a poll to the group
    await message.reply_poll(
        question=question,
        options=options,
        type="quiz",
        correct_option_id=quiz["correct"]
    )
