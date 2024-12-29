from PIL import Image, ImageDraw, ImageFont

def create_logo(text, font_size=50, logo_size=(400, 400), bg_color="white", text_color="black"):
    # Logo size and background
    img = Image.new('RGB', logo_size, color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load font
    try:
        font = ImageFont.truetype("font.ttf", font_size)
    except IOError:
        print("Default font loaded as Arial font not found.")
        font = ImageFont.load_default()

    # Get text size
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate position
    text_x = (logo_size[0] - text_width) // 2
    text_y = (logo_size[1] - text_height) // 2

    # Draw text
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Save the logo
    img.save("logo.png")
    print("Logo saved as 'logo.png'")
