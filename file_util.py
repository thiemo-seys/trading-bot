import yaml


def load_yaml(path: str):
    with open(path, "r") as file:
        data = yaml.safe_load(file)
    return data
