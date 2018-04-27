from lxml import html
import csv, os, json
import requests
from bs4 import BeautifulSoup as bs
#from exceptions import ValueError
from time import sleep


url = 'https://www.amazon.com/gp/product/B005VWUZIY'


def AmzonParser(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    page = requests.get(url, headers=headers).text
    soup = bs(page, 'lxml')

    print(page.status_code)
    print(soup)