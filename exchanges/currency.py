from dataclasses import dataclass
from typing import List, Dict

from exchanges.symbol import Symbol


@dataclass
class Currency:
    name: str
    symbols: List[Symbol]
