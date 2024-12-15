import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "").split())
)  # Input type must be interger


# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nortoxs/Quizbot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
