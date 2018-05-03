from MobileCrawler import *
from itemPlot import *
from tkinter import *
from tkinter import ttk

# Extract product's ASIN from url
def urlTK(event):
    url = enterProductBox.get()
    try:
        asin = asinGeturl(event, url)
    except:
        asin = asinGetRX(event, url)
    print('ASIN:', asin)


"""asinTracker(asin)

# Get HTML code
soup = pageGet(asin)

# Get price
try:
    price = priceGetAll(soup)
except:
    price = priceGetDeal(soup)

print('Price:', price)

# Get product's name
try:
    name = nameGet(soup)
except:
    name = nameGetOther(soup)
print('Product Name:', name)

# Get product's image
imageURL = imageGet(soup)
print('IMG url:', imageURL)

# Write data to CSV
csvAppend(asin, price, name)

# Plot data from CSV and find max, min, avg
plotItem(asin, name)
findMax(asin)
findMin(asin)
findAvg(asin)"""


"""root = Tk()
root.title('InfoLection')
frame = Frame(root)
userURL = StringVar()
rmFile = "READ ME.txt"

# ---- Create label, button, entry and text widgets into our frame. ----
# --- Create instruction label ---
yearLbl = ttk.Label(root, text='Enter Year: ')
yearLbl.grid(row=0, column=0, sticky=E)

# --- Create Year Entry Box ---
urlEntry = ttk.Entry(root)
urlEntry.grid(row=0, column=1, columnspan=3, sticky=W)
urlEntry.delete(0, END)
urlEntry.insert(0, '')

# --- Create Submit Button ---
submitBtn = ttk.Button(root, text='Submit')
submitBtn.bind('<Button-1>', userSelection)
submitBtn.grid(row=3, column=0, columnspan=5, sticky=NSEW)

# --- Keep Window Open ---
root.mainloop()"""

# GUI- by Fuster

top = Tk()
E1 = Entry(top, bd =5)


def getURL(event):
    """ Gets user's url. Outputs valid url. """
    url = enterProduct.get()
    url = urlValidator(event, url)
    print(url)



L1 = Label(top, text="Product")
enterProduct = ttk.Label(top, text='Enter Product: ')
enterProduct.grid(row=0, column=0, sticky=E)

# URL Entry box
enterProductBox = ttk.Entry(top)
enterProductBox.grid(row=0, column=1, columnspan=1, sticky=W)
enterProductBox.delete(0, END)
enterProductBox.insert(0, '')

# URL Submit button
submitBtn = ttk.Button(top, text='Submit')
submitBtn.bind('<Button-1>', urlTK)
submitBtn.grid(row=3, column=0, columnspan=5, sticky=NSEW)
nothingBtn = ttk.Button(top, text='Nothing')
nothingBtn.grid(row=4, column=0, columnspan=5, sticky=NSEW)

# Current Price, Max, Min, Avg Labels

# CSV Display

# Picture Display

# Chart Display

top.mainloop()
