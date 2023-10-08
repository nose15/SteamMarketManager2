from . http_methods import http_post, http_get
from . data_parser import parse_inventory
from . import utils


class SteamClient:
    CONFIG = {
        "app_id": 0,
        "user_id": "",
        "count": 100,
        "url": ""
    }

    def __init__(self, user_id, app_id):
        print("Steam Client")

        self.CONFIG["user_id"] = user_id
        self.CONFIG["app_id"] = app_id

        self.CONFIG["url"] = f"http://steamcommunity.com/inventory/{user_id}/{app_id}/2?l=english&count={self.CONFIG['count']}"

    def get_inventory(self) -> dict:
        # response = http_get(self.CONFIG["url"], {})
        response = utils.read_json_file("../data/inventory_mock.json")
        inventory = parse_inventory(response)

        return inventory
