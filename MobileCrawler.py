import csv
import re
import requests
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from io import BytesIO
from PIL import Image

url = 'https://www.amazon.com/gp/product/B0722DMYTN'


def pageRequest(url):
    """This function requests a webpage from the URL provided by the user."""
    headers = {
        'User-Agent': generate_user_agent(device_type='smartphone')
    }
    page = requests.get(url, timeout=5, headers=headers)
    soup = bs(page.text, 'lxml')
    print(page.status_code)

    return soup


def priceGet(soup):
    """This function extracts the price from a mobile version of a web page."""
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
    """This function extracts the name from a mobile version of a web page."""
    name = soup.find('span', id='title', class_='a-size-small')
    name = name.text
    name = name.strip()
    print(name)

    return name

def imageGet(soup):
    img = soup.find('img', class_='a-hidden')
    img = str(img)
    imgURL = re.findall('https?://.+jpg', img)
    response = requests.get(imgURL)
    img = Image.open(BytesIO(response.content))
    print(imgURL)


# **** PROGRAM ****
soup = pageRequest(url)
priceGet(soup)
nameGet(soup)
imageGet(soup)


