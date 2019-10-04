from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    pricing = {"A":50,
                "B":30,
                "C":20,
                "D":15}
    discounts = ("A","B")

    items_counter = Counter(skus)

    price = 0

    for item in items_counter:
        quantity_of_item = items_counter[item]

        if item not in discounts:
            price += pricing[item] * quantity_of_item
            continue
        
        if item == "A" and quantity_of_item >= 3:
            
        else:
            price += pricing[item] * quantity_of_item
    


    

checkout("AAABCD")




