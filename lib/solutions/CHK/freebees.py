

def apply_freebees(skus):
    freebee_list = [{"letter_needed":"E","quantity_needed":2,"letter_removal":"B"}]
    s = skus
    for freebee in freebee_list:
        number_of_discounts = int(s.count(freebee['letter_needed'])/freebee['quantity_needed'])
        if number_of_discounts < 1:
            continue
        for i in range(number_of_discounts):
            s = s.replace(freebee['letter_removal'],"",1)

    return s
