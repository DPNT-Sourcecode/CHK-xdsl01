from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    pricing = {"A":50,
                "B":30,
                "C":20,
                "D":15}
    discounts = {"A":0,
                "B":0}

    items_counter = Counter(skus)

    for item in items_counter:
        quantity_of_item = items_counter[item]
        
    

checkout("AAABC")



