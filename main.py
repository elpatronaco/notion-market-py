import io

from env import Env
from fdk import response
from client import NotionMarket, NotionMarketOpts, UpdateOpts, \
    NotionMarketHandler
from utils.filter_args import FilterArgs
from handlers import Handlers


def init_client():
    opts = NotionMarketOpts(token_v2=Env.NOTION_TOKEN_V2)

    return NotionMarket(opts)


def handler(ctx, data: io.BytesIO = None):
    try:
        client = init_client()

        opts = UpdateOpts(database_id=Env.DATABASE_ID, handlers=[
            NotionMarketHandler(name="crypto",
                                filters=FilterArgs.select_eq("Tipo", "Criptos"),
                                handler=lambda ticker: Handlers.CryptoCom(
                                    ticker)),
            # Handler(name="stocks",
            #        filters=FilterArgs.multi_select_contains("Tipo",
            #                                                 "Acciones"),
            #        handler=lambda ticker: Handler.StocksCom(ticker))
        ])
        client.update_db(opts)

        return response.Response(
            ctx,
            response_data={"message": "Success"},
        )
    except Exception as e:
        return response.Response(
            response_data=e,
            status_code=500
        )


def main():
    handler(None)


if __name__ == "__main__":
    main()
