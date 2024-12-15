from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Quiz import app


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
    try:
        # Get the first quiz data
        quiz = quiz_data[0]
        question = quiz["question"]
        options = quiz["options"]
        correct_option_id = quiz["correct"]

        # Validate inputs
        if not isinstance(question, str) or not all(isinstance(option, str) for option in options):
            await message.reply("Invalid question or options format.")
            return

        if len(question) > 255:
            await message.reply("The question is too long (max 255 characters).")
            return

        if any(len(option) > 100 for option in options):
            await message.reply("Each option must be under 100 characters.")
            return

        # Ensure correct_option_id is within the range of options
        if correct_option_id < 0 or correct_option_id >= len(options):
            await message.reply("The correct_option_id is out of range.")
            return

        # Send the quiz poll
        await message.reply_poll(
            question=question,
            options=options,
            type="quiz",
            correct_option_id=correct_option_id
        )
    except Exception as e:
        await message.reply(f"An unexpected error occurred: {e}")
        
