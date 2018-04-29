#!/usr/bin/env python3
from MobileCrawler import asinGet, pageGet, priceGet, nameGet, imageGet, csvWriter, csvAppend

""" OUR PROGRAM WILL RUN FROM THIS FILE """

# Extract product's ASIN from url
asin = asinGet()

# Get HTML code
soup = pageGet(asin)

# Get price
price = priceGet(soup)

# Get product's name
name = nameGet(soup)

# Get product's image
imageGet(soup)

# Write data to CSV
csvAppend(asin, price, name)


# Plot data from CSV and find max, min, avg

# *** WRITE GUI CODE HERE ***


