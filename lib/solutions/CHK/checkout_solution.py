from collections import Counter
import logging
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    stock = [{"item":"A",
            "core_price":50,
            "bulk_buys":[5,3],
            "bulk_buy_cost":[200,130],
            "freebees":[]},

            {"item":"B",
            "core_price":30,
            "bulk_buys":[(2,45)],
            "freebees":[]},

            {"item":"C",
            "core_price":20,
            "bulk_buys":[],
            "freebees":[]},

            {"item":"D",
            "core_price":15,
            "bulk_buys":[],
            "freebees":[]},

            {"item":"E",
            "core_price":40,
            "bulk_buys":[],
            "freebees":[{"quantity_needed":2,"freebee_item":"B","free_quantity":1}]}
            ]

    items_counter = Counter(skus)

    #Create a dict to allow us to quickly find the item in question
    stock_lookup = {}
    for index,product in enumerate(stock):
        stock_lookup[product[item]] = index

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

        if quantity_of_item < 




        
        
    return price





