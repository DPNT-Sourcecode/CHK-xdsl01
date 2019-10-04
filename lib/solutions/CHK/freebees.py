from collections import Counter

freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]
freebee_lookup = {}
for index,product in enumerate(freebee_list):
    freebee_lookup[product['letter_needed']] = index
print(freebee_lookup)
def apply_freebees(skus):
    item_counter = dict(Counter(skus))
    print(item_counter)
    for k,v in item_counter.items():
        if not freebee_lookup.get(k,None):
            continue
        
        possible_discounts = int(v/freebee_list[freebee_lookup[k]]["quantity_needed"])
        print(possible_discounts)
        letter_that_can_be_removed = freebee_list[freebee_lookup[k]]["letter_removal"]
        items_that_can_be_removed = int(possible_discounts/item_counter.get(letter_that_can_be_removed,possible_discounts+1))
        print(items_that_can_be_removed)
        if items_that_can_be_removed > 0:
            item_counter[letter_that_can_be_removed] -= items_that_can_be_removed

    print(item_counter)

apply_freebees("EEEEBB")





