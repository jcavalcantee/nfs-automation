from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
BUCKET_NAME = os.getenv("BUCKET_NAME")
CLIENT_ID = os.getenv("CLIENTE_ID")
SERVICE_VALUE = os.getenv("SERVICE_VALUE")