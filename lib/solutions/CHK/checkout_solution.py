from collections import Counter
import json
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

    items_counter = Counter(skus)

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

        #Working out the freebees
        # if item_details['freebees']:
        #     for freebee in item_details['freebees']:
        #         if items_counter[item] < freebee['quantity_needed']:
        #             continue
        #         if freebee['freebee_item'] in skus:
        #             free_item = stock[stock_lookup[freebee['freebee_item']]]
        #             price -= freebee['free_quantity']*free_item['core_price']

        if item_details['freebees']:
           for freebee in item_details['freebees']:
                if items_counter[item] < freebee['quantity_needed']:
                    continue
                possible_discounts_to_be_applied = items_counter[item]/freebee['quantity_needed']
                items_that_can_be_removed = items_counter[freebee['discounted_item']]
                number_of_items_to_remove = possible_discounts_to_be_applied/items_that_can_be_removed
                price -= int(number_of_items_to_remove)*freebee['reduction']
                
        
    return price
