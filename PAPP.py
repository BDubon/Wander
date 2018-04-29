#!/usr/bin/env python3
from MobileCrawler import asinGet, pageGet, priceGetMost, priceGetSome, nameGet, imageGet, csvAppend

""" 
             OUR PROGRAM WILL RUN FROM THIS FILE 
"""
# --- To see the functions' code, refer to MobileCrawler.py --- #

# Extract product's ASIN from url
asin = asinGet()

# Get HTML code
soup = pageGet(asin)

# Get price
try:
    price = priceGetMost(soup)
except:
    price = priceGetSome(soup)

# Get product's name
name = nameGet(soup)

# Get product's image
imageGet(soup)

# Write data to CSV
csvAppend(asin, price, name)

# Plot data from CSV and find max, min, avg



# *** WRITE GUI CODE HERE ***


