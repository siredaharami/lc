from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, font_size=50):
    """
    Adds text to the center of the image.

    Args:
        image_path (str): Path to the input image.
        text (str): Text to overlay on the image.
        font_size (int): Size of the font.

    Returns:
        str: Path to the output image.
    """
    try:
        # Open image
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

        # Add text to image
        draw.text((text_x, text_y), text, fill="white", font=font)

        # Save the modified image
        output_path = "output_image.png"
        img.save(output_path)
        return output_path
    except Exception as e:
        raise Exception(f"Error processing image: {e}")
