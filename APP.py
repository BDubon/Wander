import matplotlib
matplotlib.use('TkAgg')
from MobileCrawler import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk


class mclass:
    def __init__(self, window):
        self.window = window
        # URL Entry Box
        self.urlBox = ttk.Entry(window)
        self.urlBox.grid(row=0, column=1, columnspan=10, pady=5, padx=5, sticky=NSEW)
        self.urlBox.delete(0, END)
        self.urlBox.insert(0, '')
        # SUBMIT Button
        self.submitBtn = ttk.Button(window, text='Submit')
        self.submitBtn.bind('<Button-1>', urlTK)
        self.submitBtn.grid(row=1, column=4, columnspan=4, sticky=NSEW)

    def urlTK(self):
        url = self.urlBox.get()
        try:
            self.asin = asinGeturl(url)
        except:
            self.asin = asinGetRX(url)
        print('ASIN:', self.asin)

        return self.asin

    def asinGeturl(self):
        """ This function extracts the product's unique ASIN from an amazon.com url. """
        self.asin = self.url.split('/')
        for i in self.asin:
            self.asinNum = i.strip()
            if len(self.asinNum) != 10:
                continue
            else:
                self.asinN = self.asinNum

        return self.asinN

    # Get Page HTML Code
    def pageGet(self):
        """ This function requests a webpage from the URL provided by the user. """
        headers = {
            'User-Agent': generate_user_agent(device_type='smartphone')
        }
        self.url = 'https://www.amazon.com/gp/product/' + self.asin
        self.page = requests.get(self.url, timeout=5, headers=headers)
        self.soup = bs(self.page.text, 'lxml')
        print('Page Status:', self.page.status_code)

        return self.soup

    # Get Prices
    def priceGetAll(self):
        """ Combines existing functions into a single one. """
        try:
            self.price = priceGetMost(self.soup)
        except:
            self.price = priceGetSome(self.soup)
        print('Price: $' + str(self.price))

        return self.price





    def plot(self):
        df = pd.read_csv('CSVs/' + self.ASIN + ".csv")

        # set axis
        x = df["Date"]
        y = df["Price"]
        # Plot Data
        plt = Figure(figsize=(7, 4))
        plt.plot(x, y)
        # Add Labels
        plt.title("\n".join(wrap(name, 40)), fontsize=18)
        plt.xlabel('Date', fontsize=14)
        plt.xticks(rotation=90, fontsize=8)
        plt.ylabel('Price ($)', fontsize=14)


window = Tk()
start = mclass(window)
window.mainloop()