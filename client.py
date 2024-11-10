from dataclasses import dataclass

from notion_client import Client as NotionClient
from typing import Any, Dict, List, Optional, Type, Callable, NewType

from handlers import HandlerCbType

FiltersType = NewType("FiltersType", Dict[str, Any])
HandlerType = NewType("HandlerType", HandlerCbType)


@dataclass
class Handler:
    name: str
    cb: Type[Callable]
    filters: FiltersType


@dataclass
class NotionMarketOpts:
    token_v2: str


@dataclass
class UpdateOpts:
    database_id: str
    handlers: List[Handler]


def init_notion(token_v2: str):
    return NotionClient(auth=token_v2)


class NotionMarket:
    def __init__(self, opts: NotionMarketOpts):
        self.client = init_notion(opts.token_v2)

    def __get_db(self, database_id: str):
        return self.client.databases.retrieve(database_id=database_id)

    def __query_db(self, database_id: str,
                   filters: Optional[FiltersType] = None):
        return self.client.databases.query(
            **{
                "database_id": database_id,
                "filter": filters
            }
        )

    def __update_page(self, page_id: str):
        return self.client.pages.update(page_id=page_id, archived=False)

    async def update_db(self, opts: UpdateOpts):
        try:
            self.__get_db(opts.database_id)
        except Exception as e:
            print(f"DB not retrievable: {e}")
            return

        for handler in opts.handlers:
            pages = self.__query_db(opts.database_id, handler.filters)

            for page in pages["results"]:
                try:
                    await handler.cb(page["id"])
                except Exception as e:
                    print(f"Error updating page: {e}")
                    continue
