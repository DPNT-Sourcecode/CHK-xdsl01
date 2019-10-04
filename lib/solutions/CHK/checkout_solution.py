from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    pricing = {"A":50,
                "B":30,
                "C":20,
                "D":15}
    discounts = {"A":3,
                "B":2}

    items_counter = Counter(skus)

    price = 0

    for item in items_counter:
        quantity_of_item = items_counter[item]

        if item not in discounts:
            price += pricing[item] * quantity_of_item
            continue
        
        if quantity_of_item < discounts[item]:
            price += pricing[item] * quantity_of_item
        else:
            number_of_applicaple_discounts = quantity_of_item/discounts[item]
            print(item,int(number_of_applicaple_discounts))
            
    


    

checkout("AAAABCD")





