from PIL import Image, ImageDraw, ImageFont
import io
from config import *

async def send_edited_image(client, chat_id):
    user_data = users_data[chat_id]
    # Extract settings like opacity, inner shadow color, background, font, etc.
    opacity = user_data.get('opacity', 1)
    inner_shadow_color = user_data.get('inner_shadow_color', 'black')
    font_path = user_data.get('font', 'font.ttf')
    photo_data = user_data['photo']
    text = user_data.get('text', '')
    position = user_data.get('position', (10, 10))
    color = user_data.get('color', 'black')
    font_size = user_data.get('font_size', 40)

    # Image processing
    image = Image.open(io.BytesIO(photo_data))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Apply opacity
    image.putalpha(int(255 * opacity))  # Apply the opacity effect to the image

    # Apply other effects (inner shadow, background, font, etc.)
    # Example: Inner shadow application
    if user_data.get('inner_shadow_enabled', False):
        # Apply inner shadow logic here
        pass

    # Save image and send back to the user
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    await client.send_photo(chat_id, img_byte_arr, caption="Here is your edited logo!")
