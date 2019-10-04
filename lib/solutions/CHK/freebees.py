from collections import Counter

freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]

freebee_lookup = {}
for index,product in enumerate(freebee_list):
    freebee_lookup[product['letter_needed']] = index

def apply_freebees(skus):
    item_counter = dict(Counter(skus))
    
    for letter,occurance in item_counter.items():
        if letter not in freebee_lookup.keys():
            continue
        
        possible_discounts = int(occurance/freebee_list[freebee_lookup[letter]]["quantity_needed"])
        letter_that_can_be_removed = freebee_list[freebee_lookup[letter]]["letter_removal"]
        items_that_can_be_removed = int(possible_discounts/item_counter.get(letter_that_can_be_removed,possible_discounts+1))
        
        for discount in range(possible_discounts):
            if item_counter[letter_that_can_be_removed] > 0:
                item_counter[letter_that_can_be_removed] -= 1

    #Rebuild the string with the items taken away
    return_string = ""
    for k,v in item_counter.items():
        for i in range(v):
            return_string = return_string+k
    return return_string





