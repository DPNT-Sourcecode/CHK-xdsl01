for item in items_counter:

        if item not in pricing.keys():
            logging.info(f"{item} not in pricing library")
            return -1

        quantity_of_item = items_counter[item]

        if item not in discount_quantities:
            price += pricing[item] * quantity_of_item
            continue
        
        if quantity_of_item < discount_quantities[item]:
            price += pricing[item] * quantity_of_item
        else:
            #We need to check how many of the discounts we can apply to this item.
            number_of_applicaple_discounts = quantity_of_item/discount_quantities[item]
            #The remaining quantity goes at the standard price.
            remaining_quantity_outside_discount = quantity_of_item-(int(number_of_applicaple_discounts)*discount_quantities[item])
            #Work out the final cost for that item
            total_items_cost = (int(number_of_applicaple_discounts)*discount_offer[item]) + (remaining_quantity_outside_discount*pricing[item])
            price += total_items_cost