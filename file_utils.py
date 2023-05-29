import yaml
from yaml import SafeLoader

def load_yaml(path: str):
    with open(path) as file:
        data = yaml.load(file, Loader=SafeLoader)
        return data
