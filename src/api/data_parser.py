import json


def get_item_classes(assets: [dict], descriptions: [dict]) -> dict:
    item_classes = {}

    for asset in assets:
        class_id = asset['classid']

        if class_id in item_classes.keys():
            item_classes[class_id]['count'] += 1
            item_classes[class_id]['assets'].append(asset['assetid'])
            continue

        item_classes[class_id] = {
            'count': 1,
            'assets': [asset['assetid']]
        }

    for idx, class_id in enumerate(item_classes.keys()):
        description = descriptions[idx]
        item_classes[class_id]["name"] = description["name"]
        item_classes[class_id]["market_name"] = description['market_name']
        item_classes[class_id]["market_hash_name"] = description['market_hash_name']
        item_classes[class_id]["tradable"] = description["tradable"]
        item_classes[class_id]["marketable"] = description["marketable"]

    return item_classes


def parse_inventory(inventory_json_str: str) -> dict:
    inventory_dict = json.loads(inventory_json_str)

    assets = inventory_dict['assets']
    descriptions = inventory_dict['descriptions']

    item_classes = get_item_classes(assets, descriptions)

    return item_classes

