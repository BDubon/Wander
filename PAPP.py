#!/usr/bin/env python3
from MobileCrawler import *
from itemPlot import *
from tkinter import *
from tkinter import ttk
userURL = StringVar()

""" 
             OUR PROGRAM WILL RUN FROM THIS FILE 
"""
# --- To see the functions' code, refer to MobileCrawler.py, itemPlot.py --- #

url = getURL()
url = urlValidator(url)
userURL.get(url)



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
print('IMG url:', imageURL)

# Write data to CSV
csvAppend(asin, price, name)

# Plot data from CSV and find max, min, avg
plotItem(asin, name)
findMax(asin)
findMin(asin)
findAvg(asin)


# *** WRITE GUI CODE HERE ***
root = Tk()
root.title('PAPP')
frame = Frame(root)
userURL = StringVar()
# searchNum = IntVar()
# rmFile = "READ ME.txt"

"""# ---- Create label, button, entry and text widgets into our frame. ----
# --- Create instruction label ---
yearLbl = ttk.Label(root, text='Enter Year: ')
yearLbl.grid(row=0, column=0, sticky=E)"""

# --- Create Year Entry Box ---
yearEntry = ttk.Entry(root)
yearEntry.grid(row=0, column=1, columnspan=1, sticky=W)
yearEntry.delete(0, END)
yearEntry.insert(0, '')

"""# --- Create Submit Button ---
submitBtn = ttk.Button(root, text='Submit')
submitBtn.bind('<Button-1>', userSelection)
submitBtn.grid(row=3, column=0, columnspan=5, sticky=NSEW)

# Menu Bar
menu = Menu(root, tearoff=0)
root.config(menu=menu)
# Submenu
subMenu = Menu(menu)
menu.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label="Instructions", command=openInstruction)
subMenu.add_command(label="About", command=openAbout)
subMenu.add_command(label='Exit', command=root.quit)

# --- Radio Buttons For Different Functions ---
# Label
searchForLbl = ttk.Label(root, text='Search for: ')
searchForLbl.grid(row=1, column=0, sticky=E)
# Radio Buttons for Functions
datesRB = ttk.Radiobutton(root, text='Election Dates', command=userSelection, value=1, variable=searchNum)   # Search Election Dates
datesRB.grid(row=1, column=1, sticky=W)
candidatesRB = ttk.Radiobutton(root, text='Candidates', command=userSelection, value=2, variable=searchNum)  # Search Candidates' Information
candidatesRB.grid(row=1, column=2, sticky=W)

# --- Radio Buttons to Select Sorting Method ---
# Label
sortByLbl = ttk.Label(root, text='Sort by: ')
sortByLbl.grid(row=2, column=0, sticky=E)
# Radio Buttons
dateSortRB = ttk.Radiobutton(root, text='Date/Last Name', value=1, variable=sortNum)    # Sort by state
dateSortRB.grid(row=2, column=1, sticky=W)
stateSortRB = ttk.Radiobutton(root, text='State', value=2, variable=sortNum)      # Sort by date
stateSortRB.grid(row=2, column=2, sticky=W)
officeSortRB = ttk.Radiobutton(root, text='Office', value=3, variable=sortNum)  # Sort by Office
officeSortRB.grid(row=2, column=3, sticky=W)

# --- Text Widget To Display Data ---
data = Text(root, width=50, height=25, wrap=WORD)
data.grid(row=4, column=0, columnspan=4, sticky=NSEW)

# --- Scroll Bar ---
scroll = ttk.Scrollbar(root, command=data.yview)
data['yscrollcommand'] = scroll.set
scroll.grid(row=4, column=5, pady=3, sticky=NSEW)

# Window Icon
root.iconbitmap('InfoLectionIcon.ico')
"""
# --- Keep Window Open ---
root.mainloop()


