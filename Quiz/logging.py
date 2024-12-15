import config
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import filters

SUDOERS = filters.user()

# store all logs
logging.basicConfig(
    format="[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10),
        logging.StreamHandler(),
    ],
)

LOGGER = logging.getLogger("INFO")
