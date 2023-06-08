from exchanges.binance_adapter import BinanceAdapter


def test_binance_adapter(mocker):
    mock_client = mocker.Mock()

    mock_client.get_all_tickers.return_value = {}
    mock_client.get_ticker.return_value = {}
    mock_client.get_historical_klines.return_value = {}

    adapter = BinanceAdapter(client=mock_client)

    assert adapter.list_tickers() == []
    assert adapter.get_tickers() == []
    assert adapter.get_candle() == []
