from collections import Counter

freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]
freebee_lookup = {}
for index,product in enumerate(freebee_list):
    freebee_lookup[product['item']] = index
def apply_freebees(skus):
    item_counter = dict(Counter(skus))

    for k,v in item_counter.items():





