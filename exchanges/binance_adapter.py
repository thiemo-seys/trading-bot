from typing import Dict, List
from enum import Enum

from binance.client import Client

from .adapter import ExchangeAdapter


# TODO: check if this list is complete, or if faster than once a minute is possible
class KlineInterval(Enum):
    ONE_MINUTE = Client.KLINE_INTERVAL_1MINUTE
    THREE_MINUTES = Client.KLINE_INTERVAL_3MINUTE
    FIVE_MINUTES = Client.KLINE_INTERVAL_5MINUTE
    FIFTEEN_MINUTES = Client.KLINE_INTERVAL_15MINUTE
    THIRTY_MINUTES = Client.KLINE_INTERVAL_30MINUTE
    ONE_HOUR = Client.KLINE_INTERVAL_1HOUR
    TWO_HOURS = Client.KLINE_INTERVAL_2HOUR
    FOUR_HOURS = Client.KLINE_INTERVAL_4HOUR
    SIX_HOURS = Client.KLINE_INTERVAL_6HOUR
    EIGHT_HOURS = Client.KLINE_INTERVAL_8HOUR
    TWELVE_HOURS = Client.KLINE_INTERVAL_12HOUR
    ONE_DAY = Client.KLINE_INTERVAL_1DAY
    THREE_DAYS = Client.KLINE_INTERVAL_3DAY
    ONE_WEEK = Client.KLINE_INTERVAL_1WEEK
    ONE_MONTH = Client.KLINE_INTERVAL_1MONTH


class BinanceAdapter(ExchangeAdapter):
    def __init__(self, client: Client):
        self.client = client

    def list_tickers(self) -> List[Dict]:
        return self.client.get_all_tickers()

    def get_tickers(self, symbols: List[str]) -> List[Dict]:
        """
        24 hour price change statistics

        :param symbols: A list of symbols to get tickers for
        :return: a list of tickers in a dictionary format with keys....
        """
        if not isinstance(symbols, list):
            symbols = [symbols]

        return self.client.get_ticker(symbols)

    def get_candle(self, symbol: str, interval: KlineInterval, start_date, end_date) -> List[Dict]:
        return self.client.get_historical_klines(symbol, interval.value, start_date, end_date)

