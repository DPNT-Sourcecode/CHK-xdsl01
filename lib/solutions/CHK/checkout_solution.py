from collections import Counter
import logging
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    stock = [{"item":"A",
            "core_price":50,
            "bulk_buys":[5,3],
            "freebees":[{[]},
            {"item":"B",
            "core_price":30,
            "bulk_buys":[(2,45)],
            "freebees":[{[]},
            {"item":"C",
            "core_price":20,
            "bulk_buys":[],
            "freebees":[{[]},
            {"item":"D",
            "core_price":15,
            "bulk_buys":[],
            "freebees":[{[]},
            {"item":"E",
            "core_price":40,
            "bulk_buys":[],
            "freebees":[{"quantity_needed":2,"freebee_item":"B","free_quantity":1}]
            ]

    items_counter = Counter(skus)

    price = 0

    for item in items_counter:

        
        
    return price


