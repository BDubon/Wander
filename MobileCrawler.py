from lxml import html
import csv, os, json
import requests
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent

url = 'https://www.amazon.com/gp/product/B072Y5MZQH'


def pageRequest(url):
    headers = {
        'User-Agent': generate_user_agent(device_type='smartphone')
    }
    page = requests.get(url, timeout=5, headers=headers)
    soup = bs(page.text, 'lxml')
    print(page.status_code)

    return soup


def priceGet(soup):
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
    name = soup.find('span', id='title', class_='a-size-small')
    name = name.text
    name = name.strip()
    print(name)

    return name


soup = pageRequest(url)
priceGet(soup)
nameGet(soup)


