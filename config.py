from dataclasses import dataclass

from file_utils import load_yaml


@dataclass
class Config:
    binance_api_key: str
    logging_level: str

    @staticmethod
    def from_yaml(path: str):
        config_data = load_yaml(path)
        return Config(**config_data)
