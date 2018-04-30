import pandas as pd
import matplotlib.pyplot as plt


def plotItem(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")

    # set axis
    x = df["Date"]
    y = df["Price"]

    plt.title('Item Price Over Time', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel('Price ($)', fontsize=14)
    plt.plot(x, y)
    plt.show()


def findMax(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")
    hPrice = round(df['Price'].max(), 2)
    print(hPrice)


def findMin(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")
    lPrice = round(df['Price'].min(), 2)
    print(lPrice)


def findAvg(ASIN):

    df = pd.read_csv('CSVs/' + ASIN + ".csv")
    avgPrice = round(df['Price'].mean(), 2)
    print(avgPrice)




