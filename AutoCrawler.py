# Written by Nicholas Archer
from MobileCrawler import asinTracker
from MobileCrawler import *
def AC():
    """ This function requests data for all products previously requested and updates
    the CSV files foe its corresponding item. """
    print('--- UPDATING DATABASE ---')
    print('       Please Wait       ')
    print('')
    new_list = []    # New list to import ASIN from text file
    with open('ASINs.txt') as asin:
        for line in asin:
            line = line.strip()
            new_list.append(line)

    indiv_asin_set = set(new_list)    # Make sure we only request the item once by creating a set
    for item in indiv_asin_set:
        try:
            print('ASIN:', item)
            soup = pageGet(item)

            # Get product's name
            try:
                name = nameGet(soup)
            except:
                name = nameGetOther(soup)
            print('Product Name:', name)

            # Get price
            try:
                price = priceGetAll(soup)
            except:
                price = priceGetDeal(soup)
            print('Price: $' + str(price))

            # Add new data to CSV files for each product
            csvAppend(item, price, name)
            print('')
        except:
            print('ERROR: There was a problem with this page. Item not updated')
            print('')
            pass
    print('--- DATABASE HAS BEEN UPDATED ---')
