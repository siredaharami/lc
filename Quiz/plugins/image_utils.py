from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, text_color="black", font_size=50):
    """
    Adds text to the center of the image with the specified text color.

    Args:
        image_path (str): Path to the input image.
        text (str): Text to overlay on the image.
        text_color (str): Color of the text (e.g., 'red', 'blue', 'white').
        font_size (int): Size of the font.

    Returns:
        Image: Modified PIL Image object.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Create a drawing object
        draw = ImageDraw.Draw(img)

        # Load font
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text position
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (img.width - text_width) // 2
        text_y = (img.height - text_height) // 2

        # Add text to the image
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        return img
    except Exception as e:
        raise Exception(f"Error processing image: {e}")
