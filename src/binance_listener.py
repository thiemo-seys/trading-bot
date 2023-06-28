from enum import Enum

from binance import ThreadedWebsocketManager
from src.composite import CompositeListener


class ListenerState(Enum):
    IDLE = 0
    LISTENING = 1
    STOPPED = 2


# TODO: think about a message class
# Binance documentation: https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#individual-symbol-ticker-streams
class WebSocketListener:
    def __init__(self, socket_client: ThreadedWebsocketManager, listener: CompositeListener):
        self.socket_client = socket_client
        self.state = ListenerState.IDLE
        self.listener = listener

    def on_message(self, message):
        print(f"received message: {message}")
        if message["e"] == "error":
            self.on_error(message)

        self.listener.on_message(message)

    def on_error(self, message):
        # TODO: should we close and restart oslt?
        self.listener.on_error(message)

    def start_symbol(self, symbol: str):
        # 24h rolling window ticker statistics for a single symbol
        channel = self.socket_client.start_symbol_ticker_socket(callback=self.on_message, symbol=symbol)
        return channel


    # TODO: implement stopping channels

    def _start(self):
        self.state = ListenerState.LISTENING
        self.socket_client.start()

    def _stop(self):
        self.state = ListenerState.STOPPED
        self.socket_client.stop()
