import argparse

from binance.client import Client

from config import Config
from exchanges.binance import BinanceAdapter


def main():
    args = parser.parse_args()

    config = Config.from_yaml(args.config)

    client = Client(config.api_key, config.api_secret, testnet=True)
    adapter = BinanceAdapter(client)
    breakpoint()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='path to config file', default='configs/testnet.yaml')
    main()
