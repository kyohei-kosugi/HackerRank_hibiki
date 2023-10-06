from collections import OrderedDict
import re

n = int(input())
inventory = OrderedDict()

for _ in range(n):
    # スペースで分割して商品名と価格を取得します
    parts = input().split()
    item = " ".join(parts[:-1])  # 商品名はスペースを含むことがあるので、残りの部分を再結合します
    price = int(parts[-1])  # 価格は最後の要素です
    if item in inventory:
        inventory[item] += price
    else:
        inventory[item] = price

for item, price in inventory.items():
    print(f'{item} {price}')

    



