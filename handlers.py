from typing import Awaitable, Callable
from env import Env
from handlers.cryptocom import CryptoComHandlerOpts, CryptoComHandler

HandlerCbType = Callable[[str], Awaitable[float]]


class Handler:
    @staticmethod
    def CryptoCom(symbol: str) -> float:
        opts = CryptoComHandlerOpts(api_key=Env.CRYPTO_API_KEY,
                                    secret_key=Env.CRYPTO_SECRET_KEY)
        handler = CryptoComHandler(opts)

        try:
            return handler.get_mark_price(symbol)
        except Exception:
            return 0.0

    @staticmethod
    def StocksCom(isin: str) -> float:
        return 0.0
