import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

CACHE_DURATION = 600  # seconds (10 minutes)

if not API_KEY:
    raise EnvironmentError("WEATHER_API_KEY not found. Please set it in .env file.")
