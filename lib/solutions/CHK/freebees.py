from collections import Counter

freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]
freebee_lookup = {}
for index,product in enumerate(freebee_list):
    freebee_lookup[product['item']] = index

def apply_freebees(skus):
    item_counter = dict(Counter(skus))

    for k,v in item_counter.items():
        if not freebee_lookup.get(k,None):
            continue
        
        possible_discounts = int(v/freebee_list[freebee_lookup[k]]["quantity_needed"])
        letter_that_can_be_removed = freebee_list[freebee_lookup[k]]["letter_removal"]
        items_that_can_be_removed = int(possible_discounts/item_counter.get(letter_that_can_be_removed,possible_discounts+1))




