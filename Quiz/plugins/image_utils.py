from PIL import Image, ImageDraw, ImageFont
import io

async def send_edited_image(client, chat_id):
    user_data = users_data[chat_id]
    photo_data = user_data['photo']
    text = user_data.get('text', '')
    position = user_data.get('position', (10, 10))
    color = user_data.get('color', 'black')
    font_path = user_data.get('font_path', "Southam Demo.ttf")
    stroke_color = user_data.get('stroke_color', 'black')
    stroke_width = user_data.get('stroke_width', 2)
    stroke_enabled = user_data.get('stroke_enabled', False)
    font_size = user_data.get('font_size', 40)
    shadow_enabled = user_data.get('shadow_enabled', False)
    inner_shadow_enabled = user_data.get('inner_shadow_enabled', False)
    shadow_color = user_data.get('shadow_color', 'gray')
    shadow_offset = user_data.get('shadow_offset', (5, 5))
    shadow_size = user_data.get('shadow_size', 3)

    image = Image.open(io.BytesIO(photo_data))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Apply shadow
    if shadow_enabled:
        shadow_position = (position[0] + shadow_offset[0], position[1] + shadow_offset[1])
        for x in range(-shadow_size, shadow_size + 1):
            for y in range(-shadow_size, shadow_size + 1):
                draw.text((shadow_position[0] + x, shadow_position[1] + y), text, fill=shadow_color, font=font)

    # Apply inner shadow
    if inner_shadow_enabled:
        for x in range(-shadow_size, shadow_size + 1):
            for y in range(-shadow_size, shadow_size + 1):
                draw.text((position[0] - x, position[1] - y), text, fill=shadow_color, font=font)

    # Apply text with stroke or normal text
    if stroke_enabled:
        draw.text(position, text, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke_color)
    else:
        draw.text(position, text, fill=color, font=font)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    await client.send_photo(chat_id, img_byte_arr, caption="Here is your edited logo!")
