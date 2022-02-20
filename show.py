#!/bin/env python3
import json
import os
import sys
import requests

BASE_URL = "https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_FR/Product-Configure?pid="


def display(p: dict):
    print(f'''{p["productName"]} {p["modelYear"]} {p["selectedColorVariationDisplayValue"]} {p["price"]["sales"].get("price", {}).get("formatted")}

Coming soon:  {p['comingSoon']} {p['comingSoonReason']} {p['comingSoonMessage']} {p['masterNotAvailableBadge']} {p['hasSuccessorProduct']}
Availability: {p["availability"]['available']} {p["availability"]['messages']} {p["availability"]['inStockDate']} {p["availability"]['shippingInfo']}
Stock:        {p['hasNewStock']} {p["availability"]['onlyXLeft']} {p["availability"]['lowStock']} {p["availability"]['onlyXLeftNumber']}
Components:   {p["components"]["frame"][0]["productName"]}  {p["components"]["drivetrain"][0]["productName"]}
''')

def load_product(id: int, args: str) -> dict:
    path = 'cache/'+ str(id) + args + ".json"
    #path = "product.json"
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        r = requests.get(BASE_URL + str(id) + args)
        if r.status_code != 500:
            r.raise_for_status()
            data = r.json()
        else:
            data = {}
        with open(path, 'w') as f:
            json.dump(data, f)
        return data


def main():
    if len(sys.argv) < 3:
        print("usage: ./show.py product_id variant")
        sys.exit(1)
    raw = load_product(sys.argv[1], sys.argv[2])
    try:
        display(raw['product'])
    except KeyError:
        print(f"no product {sys.argv[1]} found")


if __name__ == "__main__":
    main()