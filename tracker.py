from dataclasses import dataclass
from typing import List

from exchanges.candlestick import CandleStick
from statistics_utils import min_max_difference


@dataclass
class Coin:
    name: str
    candlesticks: List[CandleStick]

    def calculate_price_difference(self, prev_candles: int):
        candles = self.candlesticks[-prev_candles:]
        coin_prices = [candle.close_price for candle in candles]
        return min_max_difference(coin_prices)

    def add_candlestick(self, candlestick: CandleStick):
        self.candlesticks.append(candlestick)

@dataclass
class Tracker:
    coins: List

    def get_coins_volatility(self):
        pass
