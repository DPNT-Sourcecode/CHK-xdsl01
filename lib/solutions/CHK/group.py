import json
from collections import OrderedDict
with open("stock.json",'r') as f:
    stock = json.load(f)

stock_lookup = {}
for index,product in enumerate(stock):
    stock_lookup[product['item']] = index

def group_discounts(s):
    qualifying_letters = []
    for letter in s:
        if letter in ("S","T","X","Y","Z"):
            qualifying_letters.append(letter)
    
    if len(qualifying_letters) < 3:
        return s
    
    group_discounts_allowed = int(len(qualifying_letters)/3)

    #we want to put the most expensive items into the group of 3 to make £45
    list_of_letters_and_cost =[{"item":stock[stock_lookup[letter]]['item'],
                                "core_price":stock[stock_lookup[letter]]['core_price']} for letter in qualifying_letters]
    list_of_letters_high_to_low = sorted(list_of_letters_and_cost, key=lambda letter:letter['core_price'],reverse=True)
    to_replace = [i['item'] for i in list_of_letters_high_to_low][:group_discounts_allowed*3]
    
    for letter in to_replace:
        s = s.replace(letter,"#",1)
    
    return s







