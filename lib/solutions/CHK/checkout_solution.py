from collections import Counter
import logging
# noinspection PyUnusedLocal
# skus = unicode string

"""   pricing = {"A":50,
                "B":30,
                "C":20,
                "D":15}
    discount_quantities = {"A":3,
                "B":2}
    discount_offer = {"A":130,
                        "B":45}"""


"""+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+"""
#
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
            "freebees":[{"quantity_needed":2,"freebee_item":"B","free_quantity":1}
            ]

    #Lookups for the pricing and for any discounts that may be applied
    #We use 2 dicts to confirm the discount quantities and what the offer is
 

    items_counter = Counter(skus)

    price = 0

    for item in items_counter:

        if item not in pricing.keys():
            logging.info(f"{item} not in pricing library")
            return -1

        quantity_of_item = items_counter[item]

        if item not in discount_quantities:
            price += pricing[item] * quantity_of_item
            continue
        
        if quantity_of_item < discount_quantities[item]:
            price += pricing[item] * quantity_of_item
        else:
            #We need to check how many of the discounts we can apply to this item.
            number_of_applicaple_discounts = quantity_of_item/discount_quantities[item]
            #The remaining quantity goes at the standard price.
            remaining_quantity_outside_discount = quantity_of_item-(int(number_of_applicaple_discounts)*discount_quantities[item])
            #Work out the final cost for that item
            total_items_cost = (int(number_of_applicaple_discounts)*discount_offer[item]) + (remaining_quantity_outside_discount*pricing[item])
            price += total_items_cost
        
    return price


