from dotenv import load_dotenv
import os

load_dotenv

BASE_URL_API = os.getenv("BASE_URL_API")
BASE_URL_UI = os.getenv("BASE_URL_UI")
API_KEY = os.getenv("API_KEY")