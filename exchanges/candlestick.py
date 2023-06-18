from dataclasses import dataclass

# TODO: use context to set the precision
from decimal import Decimal


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
    interval: str