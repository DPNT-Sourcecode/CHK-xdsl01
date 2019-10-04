from collections import Counter
import json
from freebees import apply_freebees
# noinspection PyUnusedLocal
# skus = unicode string

"""+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+"""

#Load out stock from a json file, otherwise this could get massive
#./lib/solutions/CHK/stock.json
with open("stock.json",'r') as f:
    stock = json.load(f)

#Create a dict to allow us to quickly find the item in question
stock_lookup = {}
for index,product in enumerate(stock):
    stock_lookup[product['item']] = index

def checkout(skus):

    freebees_removed = apply_freebees(skus)
    print(freebees_removed)

    items_counter = Counter(freebees_removed)

    price = 0

    for item in items_counter:

        if item not in stock_lookup.keys():
            return -1

        item_details = stock[stock_lookup[item]]
        quantity_of_item = items_counter[item]

        #Working out the bulk buys
        while quantity_of_item > 0:
            for i,bulk_quantity in enumerate(item_details["bulk_buys"]):
                number_of_bulk_discounts = quantity_of_item/bulk_quantity
                if number_of_bulk_discounts < 1:
                    continue
                
                price_for_this_bulk = int(number_of_bulk_discounts) * item_details["bulk_buy_cost"][i]
                price += price_for_this_bulk

                item_quantity_to_remove = int(number_of_bulk_discounts)*bulk_quantity
                quantity_of_item -= item_quantity_to_remove
                
        
    return price