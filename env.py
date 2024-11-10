import os

from dotenv import load_dotenv

load_dotenv()

class Env:
    TOKEN_V2 = os.environ.get("TOKEN_V2")
    DATABASE_ID = os.environ.get("DATABASE_ID")
    CRYPTO_API_KEY = os.environ.get("CRYPTO_API_KEY")
    CRYPTO_SECRET_KEY = os.environ.get("CRYPTO_SECRET_KEY")