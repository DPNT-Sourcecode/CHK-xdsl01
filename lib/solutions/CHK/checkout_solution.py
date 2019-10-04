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
+------+-------+------------------------+"""

#freebees - THIS WAS A SEPARATE MODULE, BUT I COULDN'T GET THE IMPORT TO WORK SO I WAS UNABLE TO DEPLOY
freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]

freebee_lookup = {}
for index,product in enumerate(freebee_list):
    freebee_lookup[product['letter_needed']] = index

def apply_freebees(skus):
    
    #create a letter dictionary so we can start removing occurances according to the freebees
    letter_dictionary = dict(Counter(skus))
    
    
    for letter,occurance in letter_dictionary.items():

        #Let's ignore the letters that don't apply discounts
        if letter not in list(freebee_lookup):
            continue

        #How many times we can apply a discount
        possible_discounts = int(occurance/freebee_list[freebee_lookup[letter]]["quantity_needed"])
        letter_that_can_be_removed = freebee_list[freebee_lookup[letter]]["letter_removal"]
        
        #Remove the letter from the string the amount of times we can
        for discount in range(possible_discounts):
            if letter_dictionary[letter_that_can_be_removed] > 0:
                letter_dictionary[letter_that_can_be_removed] -= 1

    #Rebuild the string with the letters taken away
    return_string = ""
    for letter,occurance in letter_dictionary.items():
        for i in range(occurance):
            return_string = return_string+letter
    return return_string


#Load out stock from a json file, otherwise this could get massive

with open("./lib/solutions/CHK/stock.json",'r') as f:
    stock = json.load(f)

#Create a dict to allow us to quickly find the item in question
stock_lookup = {}
for index,product in enumerate(stock):
    stock_lookup[product['item']] = index

def checkout(skus):

    #You get items for free dependant on how many you buy of other items.
    #The first port of call is to remove those items before working out your bulk purchase discounts
    freebees_removed = apply_freebees(skus)

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
