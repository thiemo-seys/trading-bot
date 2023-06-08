from dataclasses import dataclass
# use decimals to represent currency values, floats lack presicion
# TODO: set precision to something reasonable
from decimal import Decimal, getcontext

from exchanges.symbol import Symbol


@dataclass
class CandleStick:
    open_time: float
    open_price: Decimal
    high_price: Decimal
    low_price: Decimal
    close_price: Decimal
    volume: Decimal
    close_time: float
    quote_asset_volume: Decimal
    number_of_trades: int
    taker_buy_base_asset_volume: Decimal
    taker_buy_quote_asset_volume: Decimal

    symbol: Symbol
