from dataclasses import dataclass

from exchanges.currency import Currency
from exchanges.candlestick import CandleStick


@dataclass
class Symbol:
    name: str
    base_currency: Currency
    quote_currency: Currency
    candlesticks: List[CandleStick]
