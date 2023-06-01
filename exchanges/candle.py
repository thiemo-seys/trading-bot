from dataclasses import dataclass

@dataclass
class Candle:
    open: float
    high: float
    low: float
    close: float
    volume: float
    time: int
    #symbol: Symbol
    #exchange: Exchange

    @staticmethod
    def from_json(json_data: dict):
        return Candle(
            open=json_data["open"],
            high=json_data["high"],
            low=json_data["low"],
            close=json_data["close"],
            volume=json_data["volume"],
            time=json_data["time"],
#            symbol=Symbol.from_json(json_data["symbol"]),
#            exchange=Exchange.from_json(json_data["exchange"]),
        )