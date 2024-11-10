import os

class Env:
    TOKEN_V2 = os.environ.get("TOKEN_V2")
    DATABASE_ID = os.environ.get("DATABASE_ID")
    ALPACA_API_KEY = os.environ.get("ALPACA_API_KEY")
    ALPACA_SECRET_KEY = os.environ.get("ALPACA_SECRET_KEY")
    CRYPTO_API_KEY = os.environ.get("CRYPTO_API_KEY")
    CRYPTO_SECRET_KEY = os.environ.get("CRYPTO_SECRET_KEY")