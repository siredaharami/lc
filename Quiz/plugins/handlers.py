from pyrogram import Client, filters
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

    # Save text in user data
    user_data[user_id]["text"] = message.text

    # Download the image
    image_file = await client.download_media(user_data[user_id]["image_file_id"])

    # Process the image
    try:
        output_image = add_text_to_image(image_file, user_data[user_id]["text"])

        # Send the modified image back to the user
        await message.reply_document(output_image, caption="Here is your customized logo image!")
    except Exception as e:
        await message.reply_text(f"❌ An error occurred: {e}")
    finally:
        # Cleanup user data
        user_data.pop(user_id, None)
