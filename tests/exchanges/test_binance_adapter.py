from exchanges.binance_adapter import BinanceAdapter

def test_adapter():
    adapter = BinanceAdapter("test")
    assert adapter is not None