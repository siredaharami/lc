from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from io import BytesIO
from Quiz.plugins.image_utils import add_text_to_image

# Temporary storage for user data
user_data = {}

async def start_command(client, message):
    """
    Handles the /start command.
    """
    await message.reply_text(
        "👋 Welcome to the Logo Maker Bot!\n"
        "Send me an image to start creating your custom logo."
    )

async def handle_photo(client, message):
    """
    Handles photo uploads from users.
    """
    user_id = message.from_user.id
    user_data[user_id] = {"image_file_id": message.photo.file_id}
    await message.reply_text("Great! Now send me the text you want to overlay on the image.")

async def handle_text(client, message):
    """
    Handles text input for overlaying on the image.
    """
    user_id = message.from_user.id
    if user_id not in user_data or "image_file_id" not in user_data[user_id]:
        await message.reply_text("❌ Please send an image first.")
        return

    # Save the text in user data
    user_data[user_id]["text"] = message.text

    # Ask the user to select a text color
    color_buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Red", callback_data="color_red")],
            [InlineKeyboardButton("Green", callback_data="color_green")],
            [InlineKeyboardButton("Blue", callback_data="color_blue")],
            [InlineKeyboardButton("Black", callback_data="color_black")],
            [InlineKeyboardButton("White", callback_data="color_white")],
        ]
    )
    await message.reply_text("Choose a text color for your logo:", reply_markup=color_buttons)

async def handle_color_selection(client, callback_query):
    """
    Handles text color selection via inline buttons.
    """
    user_id = callback_query.from_user.id
    if user_id not in user_data or "image_file_id" not in user_data[user_id] or "text" not in user_data[user_id]:
        await callback_query.message.reply_text("❌ Please restart and send an image first.")
        return

    # Get the selected color
    color = callback_query.data.split("_")[1]
    color_mapping = {
        "red": "red",
        "green": "green",
        "blue": "blue",
        "black": "black",
        "white": "white",
    }
    text_color = color_mapping.get(color, "black")

    # Download the image
    image_file = await client.download_media(user_data[user_id]["image_file_id"])

    # Process the image
    try:
        output_image = add_text_to_image(image_file, user_data[user_id]["text"], text_color)

        # Send the modified image directly as a photo
        with BytesIO() as image_bytes:
            output_image.save(image_bytes, format="PNG")
            image_bytes.seek(0)
            await callback_query.message.reply_photo(image_bytes, caption="Here is your customized logo image!")
    except Exception as e:
        await callback_query.message.reply_text(f"❌ An error occurred: {e}")
    finally:
        # Cleanup user data
        user_data.pop(user_id, None)
