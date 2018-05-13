import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from textwrap import wrap


def plotItem(ASIN, name):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")

    # set axis
    x = df["Date"]
    y = df["Price"]
    avgPrice = round(df['Price'].mean(), 2)

    plt.title("\n".join(wrap(name, 40)), fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel('Price ($)', fontsize=14)
    plt.axhline(avgPrice, color='#d62728')
    plt.legend(('Average', 'Price'),
               loc='upper right')

    plt.plot(x, y)
    plt.show()



def findMax(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")
    hPrice = round(df['Price'].max(), 2)

    return hPrice


def findMin(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")
    lPrice = round(df['Price'].min(), 2)

    return lPrice


def findAvg(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")
    avgPrice = round(df['Price'].mean(), 2)

    return avgPrice




