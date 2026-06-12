from dotenv import load_dotenv
import os

ENV = os.getenv("ENV", "dev")
load_dotenv(f".env.{ENV}")

BASE_URL_API = os.getenv("BASE_URL_API")
BASE_URL_UI = os.getenv("BASE_URL_UI")
API_KEY = os.getenv("API_KEY")
