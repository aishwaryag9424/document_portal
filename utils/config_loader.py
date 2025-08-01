import yaml


def load_config(config_path: str = r"config\config.yaml") -> dict:
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
        print(config)
    return config

load_config("config/config.yaml")