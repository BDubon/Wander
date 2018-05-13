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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



# Extract product's ASIN from url
def urlTK(event):
    url = urlBox.get()
    try:
        asin = asinGeturl(url)
    except:
        asin = asinGetRX(url)
    print('ASIN:', asin)

    return asin


# GUI- by Fuster

root = Tk()
root.title("Wander")


def getURL(event):
    """ Gets user's url. Outputs valid url. """
    url = urlLabel.get()
    url = urlValidator(event, url)
    print(url)

def fullFunction():
    url = getURL()


appLabel = Label(root, text="Product")
urlLabel = ttk.Label(root, text='Paste URL: ')
urlLabel.grid(row=0, column=0, pady=5, sticky=E)

# URL Entry box
urlBox = ttk.Entry(root)
urlBox.grid(row=0, column=1, columnspan=12, pady=5, padx=5, sticky=NSEW)
urlBox.delete(0, END)
urlBox.insert(0, '')

# URL Submit button
submitBtn = ttk.Button(root, text='Submit')
submitBtn.bind('<Button-1>', urlTK)
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
picURL = 'https://images-na.ssl-images-amazon.com/images/I/51RIDjkXnyL._SY400_.jpg'
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
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=3, column=2, columnspan=3)

canvas._tkcanvas.grid(row=4, column=0, columnspan=12, padx=5)

# Quit Button
button = ttk.Button(master=root, text='Quit', command=sys.exit)
button.grid(row=5, column=6, pady=5)

root.mainloop()