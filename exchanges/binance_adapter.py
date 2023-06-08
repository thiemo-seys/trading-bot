import json
from typing import Dict, List
from enum import Enum

from binance.client import Client

from exchanges.binance_parser import data_to_candlestick
from exchanges.candlestick import CandleStick


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

    # TODO: consider using: get_exchange_info() to get all symbols
    # it returns whether the currency is trading as well
    def list_tickers(self) -> List[Dict]:
        ticker_data = self.client.get_all_tickers()

        return ticker_data


    # TODO: there should be a different endpoint: "" where we can provide our own date range
    # "GET /api/v3/ticker"
    def get_tickers(self, symbols: List[str]) -> List[Dict]:
        if not isinstance(symbols, list):
            symbols = [symbols]

        # super vague 'hack'
        # request library does not correctly serialize lists (or binance API does not process spaces in a list correctly)
        # so we just manually format the list into a string
        symbols = json.dumps(symbols)
        symbols = symbols.replace(" ", '')

        tickers_data = self.client.get_ticker(symbols=symbols)

        return []


    def get_candlesticks(self, symbol: str, interval: KlineInterval, start_date, end_date) -> List[CandleStick]:
        candle_data = self.client.get_historical_klines(symbol, interval.value, start_date, end_date)

        return [data_to_candlestick(data) for data in candle_data]
