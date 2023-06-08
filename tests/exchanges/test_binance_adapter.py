from exchanges.binance_adapter import BinanceAdapter, KlineInterval


# TODO: expand and split up these tests
def test_binance_adapter(mocker):
    mock_client = mocker.Mock()

    mock_client.get_all_tickers.return_value = {}
    mock_client.get_ticker.return_value = {}
    mock_client.get_historical_klines.return_value = [[1686168000000, '26489.39000000', '26493.29000000', '25881.89000000', '26358.48000000', '195.66986500', 1686171599999, '5162839.96099763', 4890, '113.90574800', '3005012.12117593', '0']]

    adapter = BinanceAdapter(client=mock_client)

    tickers_list = adapter.list_tickers()
    tickers = adapter.get_tickers(["mock_1", "mock_2"])
    candles = adapter.get_candlesticks("mock_1", KlineInterval.ONE_HOUR , "mock_3", "mock_4")

    # list_tickers
    #assert tickers_list == []

    # tickers
    #assert tickers == []

    # candles
    candle = candles[0]

    assert len(candles) == 1

    assert candle.open_time == 1686168000000
    assert candle.open_price == 26489.39000000
    assert candle.high_price == 26493.29000000
    assert candle.low_price == 25881.89000000
    assert candle.close_price == 26358.48000000
    assert candle.volume == 195.66986500
    assert candle.close_time == 1686171599999
    assert candle.quote_asset_volume == 5162839.96099763
    assert candle.number_of_trades == 4890
    assert candle.taker_buy_base_asset_volume == 113.90574800
    assert candle.taker_buy_quote_asset_volume == 3005012.12117593
