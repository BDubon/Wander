#cdef submit():
from MobileCrawler import *
from itemPlot import *
from tkinter import *
from tkinter import ttk
import io
from urllib.request import urlopen
from PIL import Image, ImageTk
# from pandastable import Table, TableModel
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
#from AutoCrawler import AC

price1=1

# Extract product's ASIN from url
def urlTK(event):
    url = urlBox.get()
    try:
        asin = asinGeturl(url)
    except:
        asin = asinGetRX(url)
    print('ASIN:', asin)

    return asin

def getURL(event):
    """ Gets user's url. Outputs valid url. """
    url = urlString.get()
    url = urlValidator(url)

    return url


def removeValue(event):
    urlBox.delete(0, 'end')

    return None

def fullFunction(event):
    url = getURL(event)
    print(url)
    # Extract product's ASIN from url
    try:
        asin = asinGeturl(url)
    except:
        asin = asinGetRX(url)
    print('ASIN:', asin)

    asinTracker(asin)


    # Get HTML code
    soup = pageGet(asin)

    # Get price
    try:
        price = priceGetAll(soup)
    except:
        price = priceGetDeal(soup)

    print('Price: $' + str(price))

    # Get product's name
    try:
        name = nameGet(soup)
    except:
        name = nameGetOther(soup)
    print('Product Name:', name)

    # --- Get product's image ---
    imageURL = imageGet(soup)
    print('IMG url:', imageURL)
    # Insert product's image in GUI
    picURL = imageURL
    pageResponse = urlopen(picURL)
    imageResult = io.BytesIO(pageResponse.read())
    pilImage = Image.open(imageResult)
    pilImage = pilImage.resize((120, 100), Image.ANTIALIAS)  # width X Height
    tk_img = ImageTk.PhotoImage(pilImage)
    label = ttk.Label(root, image=tk_img)
    label.grid(row=3, column=11, padx=5, pady=5)

    # Write data to CSV
    csvAppend(asin, price, name)

    # --- Plot data from CSV and find max, min, avg ---
    maxPrice = findMax(asin)
    minPrice = findMin(asin)
    avgPrice = findAvg(asin)
    # Print info to console
    print('Max Price: $' + str(maxPrice))
    print('Min Price: $' + str(minPrice))
    print('Avg Price: $' + str(avgPrice))
    print('')

    # Insert Data in GUI
    C_price_lab = ttk.Label(root, text='$' + str(price))
    C_price_lab.grid(row=3, column=1, padx=3, sticky=W)
    Max_price_lab = ttk.Label(root, text='$' + str(maxPrice))
    Max_price_lab.grid(row=3, column=5, padx=3, sticky=W)
    Min_price_lab = ttk.Label(root, text='$' + str(minPrice))
    Min_price_lab.grid(row=3, column=7, padx=3, sticky=W)
    Avg_price_lab = ttk.Label(root, text='$' + str(avgPrice))
    Avg_price_lab.grid(row=3, column=9, padx=3, sticky=W)

    # --- Chart Area ---
    f = plotItem(asin, name)
    a = f.add_subplot(111)

    chart = FigureCanvasTkAgg(f, master=root)
    chart.draw()
    chart.get_tk_widget().grid(row=3, column=2, columnspan=3)

    chart._tkcanvas.grid(row=4, column=0, columnspan=12, padx=5)

    a.plot()

    return asin


# GUI- by Fuster

root = Tk()
root.title("Wander")

urlString = StringVar()
imgUrlString = StringVar()
imgList = ['https://raw.githubusercontent.com/BDubon/Group_Project_326/master/Wander%20Logo.JPG']


appLabel = Label(root, text="Product")
urlLabel = ttk.Label(root, text='Enter URL ')
urlLabel.grid(row=0, column=0, pady=5, sticky=E)

# URL Entry box
urlBox = ttk.Entry(root, textvariable=urlString)
urlBox.grid(row=0, column=1, columnspan=12, pady=5, padx=5, sticky=NSEW)
#urlBox.insert(0, 'Enter Amazon.com URL')
urlBox.bind("<Button-1>", removeValue)

# URL Submit button
submitBtn = ttk.Button(root, text='Submit')
submitBtn.bind('<Button-1>', fullFunction)
submitBtn.grid(row=1, column=6, columnspan=1, sticky=NSEW)

# Current Price, Max, Min, Avg Labels
currentLabel = ttk.Label(root, text='Current Price: ')
currentLabel.grid(row=3, column=0, padx=5, sticky=E)


maxLabel = ttk.Label(root, text='Max Price: ')
maxLabel.grid(row=3, column=4, sticky=E)

minLabel = ttk.Label(root, text='Min Price: ')
minLabel.grid(row=3, column=6, sticky=E)

avgLabel = ttk.Label(root, text='AVG Price: ')
avgLabel.grid(row=3, column=8, sticky=E)

# Menu Bar
menu = Menu(root, tearoff=0)
root.config(menu=menu)
# Submenu
subMenu = Menu(menu)
menu.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label="Instructions")
subMenu.add_command(label="About")
subMenu.add_command(label='Exit', command=root.quit)

# Picture Display

picURL = 'https://raw.githubusercontent.com/BDubon/Group_Project_326/master/Wander%20Logo.JPG'
pageResponse = urlopen(picURL)
imageResult = io.BytesIO(pageResponse.read())
pilImage = Image.open(imageResult)
pilImage = pilImage.resize((120, 100), Image.ANTIALIAS)  # width X Height
tk_img = ImageTk.PhotoImage(pilImage)
label = ttk.Label(root, image=tk_img)
label.grid(row=3, column=11, padx=5, pady=5)

# Chart Display
# a tk.DrawingArea
f = Figure(figsize=(7, 4), dpi=100)
#a = f.add_subplot(111)

# a.plot()


'''canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=2, columnspan=3)

canvas._tkcanvas.grid(row=4, column=0, columnspan=12, padx=5)'''

# Chart Toolbar
#toolbar = NavigationToolbar2Tk(canvas, root)
#toolbar.update()
#toolbar._tkcanvas.pack(row=5, column=0, columnspan=12, padx=5, pady=3)

# Quit Button
button = ttk.Button(master=root, text='Quit', command=sys.exit)
button.grid(row=5, column=6, pady=5)
price1 = str(price1)



"""
# CSV Display

t = Frame(root)
pt = Table(t)
#pt.importCSV('CSVs/B06XWMBGWN.csv')
df = TableModel.getSampleData('CSVs/B06XWMBGWN.csv')
table = pt = Table(t, dataframe=df,
                   showtoolbar=True,
                   showstatusbar=True)
pt.grid(row=4, column=0, padx=5, pady=5)
pt.show()
"""

root.mainloop()

