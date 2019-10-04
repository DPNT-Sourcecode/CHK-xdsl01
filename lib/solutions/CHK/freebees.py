from collections import Counter

freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]

freebee_lookup = {}
for index,product in enumerate(freebee_list):
    freebee_lookup[product['letter_needed']] = index

def apply_freebees(skus):
    
    #create a letter dictionary so we can start removing occurances according to the freebees
    letter_dictionary = dict(Counter(skus))
    
    
    for letter,occurance in letter_dictionary.items():

        #Let's ignore the letters that don't apply discounts
        if letter not in freebee_lookup.keys():
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






