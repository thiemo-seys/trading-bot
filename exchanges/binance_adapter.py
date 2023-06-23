from typing import List
from enum import Enum

from binance.client import Client

from exchanges.candlestick import CandleStick
from exchanges.symbol import Symbol

from exchanges.binance_parser import data_to_candlestick, data_to_symbol


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


class BinanceAdapter:
    def __init__(self, client: Client):
        self.client = client

    def get_symbols(self) -> List[Symbol]:
        currencies_data = self.client.get_exchange_info()

        return [data_to_symbol(data) for data in currencies_data]

    def get_candlesticks(self, symbol: str, interval: KlineInterval, start_date, end_date) -> List[CandleStick]:
        candle_data = self.client.get_historical_klines(symbol, interval.value, start_date, end_date)

        return [data_to_candlestick(data + [interval.value]) for data in candle_data]
