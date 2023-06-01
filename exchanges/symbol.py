from dataclasses import dataclass

from .currency import Currency


@dataclass
class Symbol:
    name: str
    base_currency: Currency
