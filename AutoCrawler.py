from MobileCrawler import asinTracker
from MobileCrawler import *

new_list = []
with open('ASINs.txt') as asin:
    for line in asin:
        new_list.append(line)

    indiv_asin_set = set(new_list)
    for asin in indiv_asin_set:
        soup = pageGet(asin)
        # Get price
        try:
            price = priceGetAll(soup)
        except:
            price = priceGetDeal(soup)
        print('Price:', price)

        # Get product's name
        try:
            name = nameGet(soup)
        except:
            name = nameGetOther(soup)
        print('Product Name:', name)
        csvAppend(asin, price, name)
