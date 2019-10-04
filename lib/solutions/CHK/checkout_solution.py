from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    Items = Counter(skus)
    print(Items)

checkout("AAABC")

