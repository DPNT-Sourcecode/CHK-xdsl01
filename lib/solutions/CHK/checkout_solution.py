from collections import Counter
import json
# from lib.solutions.CHK.freebees import apply_freebees
# noinspection PyUnusedLocal
# skus = unicode string

"""+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
+------+-------+------------------------+"""

#freebees - THIS WAS A SEPARATE MODULE, BUT I COULDN'T GET THE IMPORT TO WORK SO I WAS UNABLE TO DEPLOY
def apply_freebees(skus):
    freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"},
                    {"letter_needed":"F","quantity_needed":3,"letter_removal":"F"},
                    {"letter_needed":"N","quantity_needed":3,"letter_removal":"M"},
                    {"letter_needed":"R","quantity_needed":3,"letter_removal":"Q"},
                    {"letter_needed":"U","quantity_needed":4,"letter_removal":"U"}]
    s = skus
    for freebee in freebee_list:
        number_of_discounts = int(s.count(freebee['letter_needed'])/freebee['quantity_needed'])
        if number_of_discounts < 1:
            continue
        for i in range(number_of_discounts):
            s = s.replace(freebee['letter_removal'],"",1)
    return s
#group discounts - SAME AS ABOVE
def apply_group_discounts(s):
    #Identifying the products applicable for the group discount
    qualifying_letters = []
    for letter in s:
        if letter in ("S","T","X","Y","Z"):
            qualifying_letters.append(letter)
    #Check if we have enough
    if len(qualifying_letters) < 3:
        return s
    
    group_discounts_allowed = int(len(qualifying_letters)/3)

    #we want to put the most expensive items into the group of 3 to make £45
    list_of_letters_and_cost =[{"item":stock[stock_lookup[letter]]['item'],
                                "core_price":stock[stock_lookup[letter]]['core_price']} for letter in qualifying_letters]
    list_of_letters_high_to_low = sorted(list_of_letters_and_cost, key=lambda letter:letter['core_price'],reverse=True)
    to_replace = [i['item'] for i in list_of_letters_high_to_low][:group_discounts_allowed*3]
    
    for letter in to_replace:
        s = s.replace(letter,"#",1)
    
    return s
#Load out stock from a json file, otherwise this could get massive
#./lib/solutions/CHK/
with open("stock.json",'r') as f:
    stock = json.load(f)

#Create a dict to allow us to quickly find the item in question
stock_lookup = {}
for index,product in enumerate(stock):
    stock_lookup[product['item']] = index

def checkout(skus):

    group_applied = apply_group_discounts(skus)
    #You get items for free dependant on how many you buy of other items.
    #The first port of call is to remove those items before working out your bulk purchase discounts.
    freebees_removed = apply_freebees(group_applied)

    #Now that the freebees are removed, we can go ahead and work out the cost taking the bulk
    #purchases into account.
    items_counter = Counter(freebees_removed)

    price = 0

    for item in items_counter:

        if item not in list(stock_lookup):
            return -1

        item_details = stock[stock_lookup[item]]
        quantity_of_item = items_counter[item]

        #Working out the bulk buys
        while quantity_of_item > 0:
            for i,bulk_quantity in enumerate(item_details["bulk_buys"]):
                number_of_bulk_discounts = quantity_of_item/bulk_quantity
                if number_of_bulk_discounts < 1:
                    continue
                
                price_for_this_bulk = int(number_of_bulk_discounts) * item_details["bulk_buy_cost"][i]
                price += price_for_this_bulk

                item_quantity_to_remove = int(number_of_bulk_discounts)*bulk_quantity
                quantity_of_item -= item_quantity_to_remove
    
    return price


