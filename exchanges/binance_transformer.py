# This is a class that transforms json data into python objects
# This class converts json data from the binance API
from typing import List, Dict

from exchanges.candlestick import CandleStick



class BinanceTransformer:
    def __init__(self):
        pass

    def _dict_to_candle(self, data: dict) -> CandleStick:
        # TODO: add some validation here?
        candlestick_attributes = {
            'open_time': int(data[0]),
            'open': float(data[1]),
            'high': float(data[2]),
            'low': float(data[3]),
            'close': float(data[4]),
            'volume': float(data[5]),
            'close_time': int(data[6]),
            'quote_asset_volume': float(data[7]),
            'number_of_trades': int(data[8]),
            'taker_buy_base_asset_volume': float(data[9]),
            'taker_buy_quote_asset_volume': float(data[10]),
            'ignore': float(data[11])
        }

        return CandleStick(**candlestick_attributes)

    def candles_to_objects(self, candles: List[Dict]) -> List[CandleStick]:
        return [self._dict_to_candle(candle) for candle in candles]