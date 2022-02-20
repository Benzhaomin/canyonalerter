#!/bin/env python3
import json
import os
import sys

import requests

URL = "https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_FR/Product-Configure?pid={pid}&dwvar_{pid}_pv_rahmenfarbe={color}"

def main():
    if len(sys.argv) < 4:
        print("usage: ./alert.py product_id color size")
        print("example: ./alert.py 2701 VT/BK S")
        sys.exit(1)

    product_id = sys.argv[1]
    color = sys.argv[2]
    size = sys.argv[3]

    r = requests.get(URL.format(pid=product_id, color=color))
    r.raise_for_status()
    p = r.json()['product']

    availability = None
    for v in p["variationAttributes"]:
        if v["id"] == "pv_rahmengroesse":
            for s in v["values"]:
                if s["value"]== size:
                    availability = s["availability"]
                    break
            break

    if not availability:
        print("bike not found")
        sys.exit(2)

    available = availability["available"]
    if not available:
        print(product_id, size, color, "not available yet")
        print(json.dumps(availability, indent=2))
        return

    filename = f'canyon_alerted_{product_id}_{color}_{size}'
    filename = ''.join([s for s in filename if s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'])
    filepath = os.path.join('/tmp', filename)
    if not os.path.isfile(filepath):
        print(f'READY TO ORDER AT: https://www.canyon.com{p["selectedProductUrl"]}')
        with open(filepath, 'w') as f:
            json.dump(available, f)
        sys.exit(1)
    else:
        print("already alerted")

if __name__ == "__main__":
    main()