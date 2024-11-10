from typing import Callable, Awaitable, NewType

HandlerCbType = Callable[[str], Awaitable[float]]


class Handler:
    @staticmethod
    def CryptoCom(ticker: str) -> float:
        return 0.0

    @staticmethod
    def StocksCom(isin: str) -> float:
        return 0.0
