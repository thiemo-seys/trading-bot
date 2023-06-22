from dataclasses import dataclass
from typing import List

import numpy as np

from exchanges.candlestick import CandleStick


@dataclass
class Coin:
    name: str
    candlesticks: List[CandleStick]

    def _get_candles_by_interval(self, interval: str):
        pass

    # TODO: @Thiemo Split of the statistics logic to a seperate functions file, no need to make a class for this
    def calculate_volatility(self, time_interval: str):
        candles = self._get_candles_by_interval(time_interval)
        coin_prices = [candle.close_price for candle in candles]

        returns = np.diff(coin_prices) / coin_prices[:-1]
        volatility = np.std(returns) * np.sqrt(len(coin_prices))
        return volatility


    def calculate_price_difference(self, time_interval: str):
        candles = self._get_candles_by_interval(time_interval)
        coin_prices = [candle.close_price for candle in candles]

        # TODO: not verry efficient, can be done in one pass
        # TODO: but it is readable, so works for now.. and a regular loop might be slower depending on the python internals implenation of min/max/index
        lowest_price = min(coin_prices)
        highest_price = max(coin_prices)
        price_difference = highest_price - lowest_price

        lowest_price_index = coin_prices.index(lowest_price)
        highest_price_index = coin_prices.index(highest_price)

        if lowest_price_index < highest_price_index:
            return price_difference
        return -price_difference


@dataclass
class Tracker:
    coins: List

    def get_coins_volatility(self):
        pass