import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"

## Get it from @Botfather in Telegram.
BOT_TOKEN = "7796646089:AAG3yoXJRSI-D2A5w1kPraju_qpL_Xt3JO8"

# Your User ID.
OWNER_ID = 7009601543


# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/siredaharami/lc",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

users_data = {}
