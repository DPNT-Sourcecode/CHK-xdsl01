from collections import Counter
import logging
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    stock = [{"item":"A",
            "core_price":50,
            "bulk_buys":[5,3,1],
            "bulk_buy_cost":[200,130,50],
            "freebees":[]},

            {"item":"B",
            "core_price":30,
            "bulk_buys":[2,1],
            "bulk_buy_cost":[45,30],
            "freebees":[]},

            {"item":"C",
            "core_price":20,
            "bulk_buys":[1],
            "bulk_buy_cost":[20],
            "freebees":[]},

            {"item":"D",
            "core_price":15,
            "bulk_buys":[1],
            "bulk_buy_cost":[15],
            "freebees":[]},

            {"item":"E",
            "core_price":40,
            "bulk_buys":[1],
            "bulk_buy_cost":[40],
            "freebees":[{"quantity_needed":2,"freebee_item":"B","free_quantity":1}]}
            ]

    items_counter = Counter(skus)

    #Create a dict to allow us to quickly find the item in question
    stock_lookup = {}
    for index,product in enumerate(stock):
        stock_lookup[product['item']] = index

    price = 0

    """+------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+"""

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

        if item_details['freebees']:
            for freebee in item_details['freebees']:
                if items_counter[item] < freebee['quantity_needed']:
                    continue
                if freebee['freebee_item'] in skus:
                    free_item = stock[stock_lookup[freebee['freebee_item']]]
                    price -= freebee['free_quantity']*free_item['core_price']

    print(price)

        
        
    return price

checkout("AAAAAAEEBD6")



