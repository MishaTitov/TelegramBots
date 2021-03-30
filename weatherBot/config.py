import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
API_KEY = os.getenv("API_KEY")
WEATHER_URL = os.getenv("WEATHER_URL")
