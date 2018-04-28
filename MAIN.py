import requests as req
from bs4 import BeautifulSoup as bs
import arrow

# URL = 'https://smile.amazon.com/Passengers-Headlight-Headlamp-Replacement-33101-SDA-A01/dp/B007TY6MK2/'
# Root URL: https://www.amazon.com/gp/product/ + ASIN

# Enter ASIN
userLink = input('Enter Link: ')


# Extract ASIN from user URL
asin = userLink.split('/')
asinN = None
for i in asin:
    asinNum = i.strip()
    if len(asinNum) != 10:
        continue
    else:
        asinN = asinNum


URL = 'https://www.amazon.com/gp/product/' + asinN

# Spoof Amazon
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

# Request Page
page = req.get(URL, headers=headers)

# Status code
print(page.status_code)

# HTML Code
soup = bs(page.text, 'lxml')

# Extract Name
name = soup.find('span', id='productTitle', class_='a-size-large')
name = name.text
name = name.strip()

# Extract Price
price = soup.find('span', id='priceblock_ourprice', class_='a-size-medium a-color-price')
price = price.text
price = price.strip()
price = price.lstrip('$')
price = float(price)

# Print extracted data
print('Name:', name)
print('Price:', price)
print('ASIN:', asinN)


# CSV Writer
with open(asinN + '.csv', 'w') as newWrite:
    date = arrow.now().format('YYYY/MM/DD')
    headerRow = 'Date,ASIN,Price,Name\n'
    newWrite.write(headerRow)
    row = date+ ',' + asinN + ',' + str(price) + ',' + name
    newWrite.write(row)


