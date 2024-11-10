import os
import io

from fdk import response
from client import NotionMarket, NotionMarketOpts, UpdateOpts
from utils.filter_args import FilterArgs
from handlers import Handler


class Env:
    TOKEN_V2 = os.environ.get("TOKEN_V2")
    DATABASE_ID = os.environ.get("DATABASE_ID")


def init_client():
    opts = NotionMarketOpts(token_v2=Env.TOKEN_V2)

    return NotionMarket(opts)


def handler(ctx, data: io.BytesIO = None):
    client = init_client()

    opts = UpdateOpts(database_id=Env.DATABASE_ID, handlers=[
        Handler(name="crypto",
                filters=FilterArgs.select_eq("Tipo", "Criptos"),
                handler=lambda ticker: Handler.CryptoCom(ticker)),
        Handler(name="stocks",
                filters=FilterArgs.multi_select_contains("Tipo", "Acciones"),
                handler=lambda ticker: Handler.StocksCom(ticker))
    ])
    client.update_db(opts)
