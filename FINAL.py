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
price1=1

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

    print('Price:', price)

    # Get product's name
    try:
        name = nameGet(soup)
    except:
        name = nameGetOther(soup)
    print('Product Name:', name)

    # Get product's image
    imageURL = imageGet(soup)
    imgList.append(imageURL)
    print('IMG url:', imageURL)

    # Write data to CSV
    csvAppend(asin, price, name)

    # Plot data from CSV and find max, min, avg
    maxPrice = findMax(asin)
    minPrice = findMin(asin)
    avgPrice = findAvg(asin)

    print('Max Price: $' + str(maxPrice))
    print('Min Price: $' + str(minPrice))
    print('Avg Price: $' + str(avgPrice))
    print('')

    plotItem(asin, name)
    price1=price
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
avgLabel.grid(row=3, column=7, sticky=E)

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
if len(imgList) < 2:
    picURL = imgList[0]
    pageResponse = urlopen(picURL)
    imageResult = io.BytesIO(pageResponse.read())
    pilImage = Image.open(imageResult)
    pilImage = pilImage.resize((100, 100), Image.ANTIALIAS)  # width X Height
    tk_img = ImageTk.PhotoImage(pilImage)
    label = ttk.Label(root, image=tk_img)
    label.grid(row=3, column=11, padx=5, pady=5)
else:
    picURL = imgList[1]
    pageResponse = urlopen(picURL)
    imageResult = io.BytesIO(pageResponse.read())
    pilImage = Image.open(imageResult)
    pilImage = pilImage.resize((100, 100), Image.ANTIALIAS)  # width X Height
    tk_img = ImageTk.PhotoImage(pilImage)
    label = ttk.Label(root, image=tk_img)
    label.grid(row=3, column=11, padx=5, pady=5)

# Chart Display
# a tk.DrawingArea
f = Figure(figsize=(7, 4), dpi=100)
a = f.add_subplot(111)


#plt.title("\n".join(wrap(name, 40)), fontsize=18)
#plt.xlabel('Date', fontsize=14)
#plt.xticks(rotation=90, fontsize=8)
#plt.ylabel('Price ($)', fontsize=14)
#plt.axhline(avgPrice, color='#d62728')
#plt.legend(('Average', 'Price'),
           #loc='upper right')
a.plot()


canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=2, columnspan=3)

canvas._tkcanvas.grid(row=4, column=0, columnspan=12, padx=5)

# Chart Toolbar
#toolbar = NavigationToolbar2Tk(canvas, root)
#toolbar.update()
#toolbar._tkcanvas.pack(row=5, column=0, columnspan=12, padx=5, pady=3)

# Quit Button
button = ttk.Button(master=root, text='Quit', command=sys.exit)
button.grid(row=5, column=6, pady=5)
price1=str(price1)
#display current price


#entry = ttk.Entry.insert(root, 12, "new ")
#entry.grid( row=3, column=1, padx=5, sticky=E)
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

