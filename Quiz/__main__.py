import asyncio
from Quiz import app  # Import the bot instance from __init__.py
from pyrogram import idle

async def main():
      await app.start()
      await idle()
  
# Start the bot
if __name__ == "__main__":
    print("Quiz bot started successfully")
    asyncio.run(main())
