import csv
import re
import requests
import arrow
import os.path
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from io import BytesIO
from PIL import Image, ImageTk

# *** WEB CRAWLER FUNCTIONS ***

def  getURL(event):
    """ Gets user's url. """
    url = input('Paste URL: ')

    return url

def urlValidator(url):
    if 'amazon.com/' not in url:
        print('ERROR: Please enter a valid amazon.com URL.')
        quit()
    elif 'smile.amazon.com/' not in url:
        print('ERROR: Please enter a valid amazon.com URL.')
        quit()
    else:
        validURL = url

    return url



def asinGeturl(url):
    """ This function extracts the product's unique ASIN from an amazon.com url. """
    asin = url.split('/')
    for i in asin:
        asinNum = i.strip()
        if len(asinNum) != 10:
            continue
        else:
            asinN = asinNum

    return asinN


def asinGetRX(url):
    """ For some pages, we extract the ASIN using RegEx. """
    asin = re.findall('[B].+[?]', url)
    asin = asin[0]
    asin = asin.rstrip('?')

    return asin



def pageGet(asin):
    """ This function requests a webpage from the URL provided by the user. """
    headers = {
        'User-Agent': generate_user_agent(device_type='smartphone')
    }
    url = 'https://www.amazon.com/gp/product/' + asin
    page = requests.get(url, timeout=5, headers=headers)
    soup = bs(page.text, 'lxml')
    print('Page Status:', page.status_code)

    return soup


def priceGetMost(soup):
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


def priceGetSome(soup):
    """ Auxiliary price extraction function. """
    price = soup.find('span', id='priceblock_ourprice', class_='a-size-medium a-color-price')
    price = price.text
    price = price.strip()
    price = price.lstrip('$')
    price = float(price)

    return price


def priceGetDeal(soup):
    """ Auxiliary price extraction function. Gets price of 'Deal of the Day'. """
    price = soup.find('td', id='priceblock_dealprice', class_='a-color-price a-size-medium')
    price = price.text
    priceList = price.split()
    price = priceList[0]
    price = price.strip()
    price = price.lstrip('$')
    price = float(price)

    return price


def priceGetAll(soup):
    """ Combines existing functions into a single one. """
    try:
        price = priceGetMost(soup)
    except:
        price = priceGetSome(soup)

    return price


def nameGet(soup):
    """ This function extracts the name from a mobile version of a web page. """
    name = soup.find('span', id='title', class_='a-size-small')
    name = name.text
    name = name.strip()

    return name


def nameGetOther(soup):
    """ This function extracts the name from a mobile version of a web page. """
    name = soup.find('h1', id='title', class_='a-size-medium')
    name = name.text
    name = name.strip()

    return name


def imageGet(soup):
    """ This function extracts the url for the image of the product. """
    img = soup.find('img', class_='a-hidden')
    img = str(img)
    imgURL = re.findall('https?://.+jpg', img)
    response = requests.get(imgURL[0])
    photo = Image.open(BytesIO(response.content))
    img = imgURL[0]

    return img

def imageGetAlt(soup):
    """ This function extracts the url for the image of the product. """
    img = soup.find('img', id='main-image', class_='imageLeft0 altImage')
    img = str(img)
    imgURL = re.findall('https?://.+jpg', img)
    response = requests.get(imgURL[0])
    photo = Image.open(BytesIO(response.content))
    img = imgURL[0]

    return img


def csvWriter(asin, price, name):
    # NOT USED
    """ Use this function when a product is first looked up. It'll
    create a new csv file to which we can append future data. """
    date = arrow.now().format('YYYY/MM/DD')
    headers = ['Date', 'ASIN', 'Price', 'Name']
    with open('CSVs/' + asin + '.csv', 'w') as newWrite:
        writer = csv.writer(newWrite)


def csvAppend(asin, price, name):
    """ Use this function when a product is already being tracked. It'll
        append data to an existing csv file. """
    file_exists = os.path.isfile('CSVs/' + asin + '.csv')  # Check if file exists
    date = arrow.now().format('YYYY/MM/DD HH:mm:ss')
    headers = ['Date', 'ASIN', 'Price', 'Name']

    with open('CSVs/' + asin + '.csv', 'a') as appendWrite:
        writer = csv.DictWriter(appendWrite, fieldnames=headers, delimiter=',', lineterminator='\n')
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Date': date, 'ASIN': asin, 'Price': price, 'Name': name.encode('utf-8').strip()})


def asinTracker(asin):
    asinList = list()
    asinSet = asinList
    asinList.append(asin)
    with open('ASINs.txt', 'a') as f:
        for i in asinSet:
            f.write(i + '\n')
