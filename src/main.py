from api.steam_client import SteamClient


def main():
    print("Steam Market Manager 2")

    steam_client = SteamClient("76561198243760718", 730)
    inventory = steam_client.get_inventory()
    print(inventory)


if __name__ == '__main__':
    main()
