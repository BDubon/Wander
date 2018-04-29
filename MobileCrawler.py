import csv
import re
import requests
import arrow
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from io import BytesIO
from PIL import Image, ImageTk

# WEB CRAWLER FUNCTIONS


def asinGet():
    """ This function extracts the product's unique ASIN. """
    url = input('Paste URL: ')
    asin = url.split('/')
    for i in asin:
        asinNum = i.strip()
        if len(asinNum) != 10:
            continue
        else:
            asinN = asinNum

    return asinN


def pageGet(asin):
    """ This function requests a webpage from the URL provided by the user. """
    headers = {
        'User-Agent': generate_user_agent(device_type='smartphone')
    }
    url = 'https://www.amazon.com/gp/product/' + asin
    page = requests.get(url, timeout=5, headers=headers)
    soup = bs(page.text, 'lxml')
    print(page.status_code)

    return soup


def priceGet(soup):
    """ This function extracts the price from a mobile version of a web page. """
    main = soup.find('span', class_='price-large')
    main = main.text
    main = main.strip()
    main = float(main)
    # Extract Cents
    centsList = soup.findAll('span', class_='a-size-small price-info-superscript')
    cents = centsList[1]
    cents = cents.text
    cents = cents.strip()
    cents = '.' + cents
    cents = float(cents)
    price = main + cents
    print(price)

    return price


def nameGet(soup):
    """ This function extracts the name from a mobile version of a web page. """
    name = soup.find('span', id='title', class_='a-size-small')
    name = name.text
    name = name.strip()
    print(name)

    return name


def imageGet(soup):
    """ This function extracts the url for the image of the product. """
    img = soup.find('img', class_='a-hidden')
    img = str(img)
    imgURL = re.findall('https?://.+jpg', img)
    response = requests.get(imgURL[0])
    photo = Image.open(BytesIO(response.content))
    print(imgURL[0])


def csvWriter(asin, price, name):
    """ Use this function when a product is first looked up. It'll
    create a new csv file to which we can append future data. """
    with open('CSVs/' + asin + '.csv', 'w') as newWrite:
        date = arrow.now().format('YYYY/MM/DD')
        headerRow = 'Date,ASIN,Price,Name\n'
        newWrite.write(headerRow)
        row = date + ',' + asin + ',' + str(price) + ',' + name
        newWrite.write(row)


