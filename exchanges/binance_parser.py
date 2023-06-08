from exchanges.candlestick import CandleStick


def data_to_candlestick(data: dict) -> CandleStick:
    candlestick_attributes = {
        'open_time': int(data[0]),
        'open_price': float(data[1]),
        'high_price': float(data[2]),
        'low_price': float(data[3]),
        'close_price': float(data[4]),
        'volume': float(data[5]),
        'close_time': int(data[6]),
        'quote_asset_volume': float(data[7]),
        'number_of_trades': int(data[8]),
        'taker_buy_base_asset_volume': float(data[9]),
        'taker_buy_quote_asset_volume': float(data[10]),
        'ignore': float(data[11]) # TODO: not sure if we want to store this
    }

    return CandleStick(**candlestick_attributes)