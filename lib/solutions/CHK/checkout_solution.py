from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items_counter = Counter(skus)

    for item in items_counter:
        quantity_of_item = items_counter[item]
        print(item,quantity_of_item)
    

checkout("AAABC")


