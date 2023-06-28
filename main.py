import argparse

from binance import ThreadedWebsocketManager

from config import Config
from src.log_util import get_logger
from src.binance_listener import WebSocketListener
from src.message_handler import LogHandler
from src.composite import CompositeListener


def main():
    args = parser.parse_args()

    config = Config.from_yaml(args.config)
    client = ThreadedWebsocketManager(config.api_key, config.api_secret, testnet=True)

    logger = get_logger(__name__)
    log_handler = LogHandler(logger)
    handlers = [log_handler]

    composite_handler = CompositeListener(handlers)

    binance_listener = WebSocketListener(client, composite_handler)
    binance_listener._start()
    binance_listener.start_symbol('BNBBTC')




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='path to config file', default='configs/testnet.yaml')
    main()
