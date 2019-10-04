import json
from collections import OrderedDict
with open("stock.json",'r') as f:
    stock = json.load(f)

stock_lookup = {}
for index,product in enumerate(stock):
    stock_lookup[product['item']] = index

def rplace_group(s):
    qualifying_letters = []
    for letter in s:
        if letter in ("S","T","X","Y","Z"):
            qualifying_letters.append(letter)
    
    if len(qualifying_letters) < 3:
        return s
    
    group_discounts_allowed = int(len(qualifying_letters)/3)

    print(group_discounts_allowed)


rplace_group("ZSYYY")




