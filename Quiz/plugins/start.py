from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Quiz.plugins.handlers import handle_photo, handle_text, handle_callback_query
from Quiz import app
from config import *

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the Logo Maker Bot!\nPlease send me an image.")

# Opacity button: "+" and "-" will adjust opacity.
@app.on_callback_query(filters.regex('opacity'))
async def opacity_buttons(client, callback_query):
    chat_id = callback_query.message.chat.id
    action = callback_query.data.split(":")[1]  # Get + or -
    
    if action == "increase":
        users_data[chat_id]['opacity'] = min(users_data[chat_id].get('opacity', 1) + 0.1, 1)
    elif action == "decrease":
        users_data[chat_id]['opacity'] = max(users_data[chat_id].get('opacity', 1) - 0.1, 0)
    
    # Update image with new opacity
    await send_edited_image(client, chat_id)

# Inner Shadow Color button
@app.on_callback_query(filters.regex('inner_shadow'))
async def inner_shadow_button(client, callback_query):
    chat_id = callback_query.message.chat.id
    # Assuming we have a list of 8 colors, we can cycle through them
    colors = ['black', 'gray', 'red', 'blue', 'green', 'purple', 'yellow', 'orange']
    current_color = users_data[chat_id].get('inner_shadow_color', 'black')
    current_index = colors.index(current_color)
    next_color = colors[(current_index + 1) % len(colors)]  # Get next color
    users_data[chat_id]['inner_shadow_color'] = next_color

    # Update image with new inner shadow color
    await send_edited_image(client, chat_id)

# Text Background button
@app.on_callback_query(filters.regex('background'))
async def background_button(client, callback_query):
    chat_id = callback_query.message.chat.id
    action = callback_query.data.split(":")[1]  # Get color or gradient
    
    if action == "color":
        # Cycle through 8 colors
        colors = ['black', 'red', 'green', 'blue', 'purple', 'orange', 'yellow', 'gray']
        current_color = users_data[chat_id].get('background_color', 'black')
        current_index = colors.index(current_color)
        next_color = colors[(current_index + 1) % len(colors)]
        users_data[chat_id]['background_color'] = next_color
    elif action == "gradient":
        # Cycle through 4 gradient colors
        gradient_colors = ['#FF6347', '#FFFF00', '#008080', '#9400D3']  # Example gradients
        current_gradient = users_data[chat_id].get('background_gradient', '#FF6347')
        current_index = gradient_colors.index(current_gradient)
        next_gradient = gradient_colors[(current_index + 1) % len(gradient_colors)]
        users_data[chat_id]['background_gradient'] = next_gradient

    # Update image with new background
    await send_edited_image(client, chat_id)

# Font button (to cycle through fonts)
@app.on_callback_query(filters.regex('font'))
async def font_button(client, callback_query):
    chat_id = callback_query.message.chat.id
    fonts = ['font1.ttf', 'font2.ttf', 'font3.ttf', 'font4.ttf', 'font5.ttf', 'font6.ttf', 'font7.ttf', 'font8.ttf', 'font9.ttf', 'font10.ttf']
    current_font = users_data[chat_id].get('font', 'font1.ttf')
    current_index = fonts.index(current_font)
    next_font = fonts[(current_index + 1) % len(fonts)]
    users_data[chat_id]['font'] = next_font

    # Update image with new font
    await send_edited_image(client, chat_id)

# Add other handlers
app.add_handler(handle_photo)
app.add_handler(handle_text)
app.add_handler(handle_callback_query)
