from typing import Dict, List

from binance.client import Client

from .exchange import ExchangeAdapter


class BinanceAdapter(ExchangeAdapter):
    def __init__(self, client: Client):
        self.client = client

    def list_tickers(self) -> List[Dict]:
        return self.client.get_all_tickers()

    # TODO: the two methods below might be a bit redundant, could probably be comined into a single function

    def get_tickers(self, symbols: List[str]) -> List[Dict]:
        """
        24 hour price change statistics

        :param symbols: A list of symbols to get tickers for
        :return: a list of tickers in a dictionary format
        """
        if not isinstance(symbols, list):
            symbols = [symbols]

        return self.client.get_ticker(symbols)
