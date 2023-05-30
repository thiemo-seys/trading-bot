from dataclasses import dataclass

from file_util import load_yaml


@dataclass
class Config:
    api_key: str
    api_secret: str

    @staticmethod
    def from_yaml(path: str):
        config_data = load_yaml(path)
        return Config(**config_data)