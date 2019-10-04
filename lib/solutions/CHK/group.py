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

    od = {}
    for letter in qualifying_letters:
        od[stock[stock_lookup[letter]]["item"]] = stock[stock_lookup[letter]]["core_price"]
    
    sorted_od = OrderedDict(od)

    qualifying_letters_highest_val_to_lowest = list(sorted_od)
    print(qualifying_letters_highest_val_to_lowest)


rplace_group("ZSTXY")



