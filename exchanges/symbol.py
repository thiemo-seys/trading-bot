from typing import List
from dataclasses import dataclass


@dataclass
class Symbol:
    name: str
    base_currency: str
    quote_currency: str
    status: str
    order_types: List[str]
