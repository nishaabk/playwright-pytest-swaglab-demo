import json
from pathlib import Path

class ConfigReader:

    @staticmethod
    def get_config():
        config_path = Path(__file__).parent.parent / "config" / "config.json"

        with open(config_path, "r") as file:
            return json.load(file)