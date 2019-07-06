basket = ['cucumber', 12, 'pickles', 4, 'sugar', 8, 'rice', 17]

def get_basket_sum(basket):
    return sum(basket[1::2]), basket[0::2]


summe, waren = get_basket_sum(basket)

print(summe)
print(waren)

