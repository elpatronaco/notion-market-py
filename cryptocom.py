import requests
import json
import secrets

from dataclasses import dataclass


@dataclass
class CryptoComHandlerOpts:
    api_key: str
    secret_key: str


class CryptoComHandler:
    def __init__(self, opts: CryptoComHandlerOpts):
        self.base_url = "https://api.crypto.com/exchange/v1"
        self.api_key = opts.api_key
        self.secret_key = opts.secret_key

    def __gen_request_id(self):
        return secrets.randbelow(100000)

    def __make_request(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"

        headers = {
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers, params=params)

        return json.loads(response.text)

    def get_mark_price(self, symbol: str) -> float:
        method = "public/get-valuations"

        params = {
            "instrument_name": symbol,
            "valuation_type": "mark_price",
        }

        res = self.__make_request(method, params)

        if res["code"] != 0:
            raise Exception(f"Error: {res['msg']}")

        return float(res["result"]["data"][0]['v'])
