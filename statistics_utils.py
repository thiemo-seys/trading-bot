from typing import List

from enum import Enum


class ReturnType(Enum):
    ABSOLUTE = 0
    RELATIVE = 1


# TODO: unit tests
# TODO: add comments -> explain the if..else.. logic
def min_max_difference(values: List, return_type: ReturnType = ReturnType.RELATIVE) -> float:
    lowest_price = min(values)
    highest_price = max(values)
    price_difference = highest_price - lowest_price

    lowest_price_index = values.index(lowest_price)
    highest_price_index = values.index(highest_price)

    if lowest_price_index > highest_price_index:
        price_difference = -price_difference
        if return_type == ReturnType.RELATIVE:
            price_difference = price_difference / lowest_price
    else:
        if return_type == ReturnType.RELATIVE:
            price_difference = price_difference / highest_price

    return price_difference
