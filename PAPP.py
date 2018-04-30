#!/usr/bin/env python3
from MobileCrawler import *
from itemPlot import *


""" 
             OUR PROGRAM WILL RUN FROM THIS FILE 
"""
# --- To see the functions' code, refer to MobileCrawler.py, itemPlot.py --- #

url = getURL()
if 'www.amazon.com/' not in url:
    print('ERROR: Please enter a valid amazon.com URL.')
    quit()

# Extract product's ASIN from url
try:
    asin = asinGet(url)
except:
    asin = asinGetRX(url)
print('ASIN:', asin)

asinTracker(asin)

# Get HTML code
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

# Get product's image
imageURL = imageGet(soup)
print('IMG url:', imageURL)

# Write data to CSV
csvAppend(asin, price, name)

# Plot data from CSV and find max, min, avg
plotItem(asin, name)
findMax(asin)
findMin(asin)
findAvg(asin)


# *** WRITE GUI CODE HERE ***


