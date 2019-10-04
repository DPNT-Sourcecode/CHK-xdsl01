from collections import Counter
import logging
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    #Lookups for the pricing and for any discounts that may be applied
    #We use 2 dicts to confirm the discount quantities and what the offer is
    pricing = {"A":50,
                "B":30,
                "C":20,
                "D":15}
    discounts = {"A":3,
                "B":2}
    discounts_offer = {"A":130,
                        "B":45}

    items_counter = Counter(skus)

    price = 0

    for item in items_counter:

        if item not in pricing.keys():
            logging.info(f"{item} not in pricing library")
            continue

        quantity_of_item = items_counter[item]

        if item not in discounts:
            price += pricing[item] * quantity_of_item
            continue
        
        if quantity_of_item < discounts[item]:
            price += pricing[item] * quantity_of_item
        else:
            number_of_applicaple_discounts = quantity_of_item/discounts[item]
            remaining_quantity_outside_discount = quantity_of_item-(int(number_of_applicaple_discounts)*discounts[item])
            total_items_cost = (int(number_of_applicaple_discounts)*discounts_offer[item]) + (remaining_quantity_outside_discount*pricing[item])
            price += total_items_cost
        
    return price



