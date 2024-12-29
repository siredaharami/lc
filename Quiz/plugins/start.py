from pyrogram import Client, filters
from Quiz.plugins.logomaker import create_logo
from Quiz import app

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Welcome to the Logo Maker Bot!\n"
        "I can help you create custom logos easily.\n\n"
        "Type /create to start making a logo."
    )

@app.on_message(filters.command("create"))
async def create(client, message):
    await message.reply_text(
        "Let's create a logo!\n\n"
        "Please send the text for your logo."
    )
    
    # Wait for user's response
    @app.on_message(filters.text & ~filters.command)
    async def logo_text(client, text_message):
        logo_text = text_message.text
        await text_message.reply_text(
            "Great! Now, please provide additional details:\n"
            "1. Font size (e.g., 50)\n"
            "2. Logo size (e.g., 400x400)\n"
            "3. Background color (e.g., white)\n"
            "4. Text color (e.g., black)\n\n"
            "Send these details in the format:\n"
            "`font_size,width,height,bg_color,text_color`",
            parse_mode="markdown"
        )

        @app.on_message(filters.text & ~filters.command)
        async def logo_details(client, detail_message):
            try:
                details = detail_message.text.split(",")
                font_size = int(details[0])
                width = int(details[1])
                height = int(details[2])
                bg_color = details[3]
                text_color = details[4]

                # Create logo
                create_logo(
                    text=logo_text,
                    font_size=font_size,
                    logo_size=(width, height),
                    bg_color=bg_color,
                    text_color=text_color
                )

                await detail_message.reply_document("logo.png", caption="Here is your logo!")
            except Exception as e:
                await detail_message.reply_text(f"❌ Error: {e}\nPlease try again with correct details.")
