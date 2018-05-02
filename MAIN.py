import requests as req
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
import arrow
from tkinter import *
from tkinter import ttk

def  getURL():
    """ Gets user's url. """
    url = input('Paste URL: ')

    return url

def urlValidator(event, url):
    if 'amazon.com/' not in url:
        print('ERROR: Please enter a valid amazon.com URL.')
        quit()
    elif 'smile.amazon.com/' not in url:
        print('ERROR: Please enter a valid amazon.com URL.')
        quit()
    else:
        validURL = url

    return validURL


root = Tk()
root.title('InfoLection')
frame = Frame(root)
sortNum = IntVar()
searchNum = IntVar()
rmFile = "READ ME.txt"

# ---- Create label, button, entry and text widgets into our frame. ----
# --- Create instruction label ---
yearLbl = ttk.Label(root, text='Enter Year: ')
yearLbl.grid(row=0, column=0, sticky=E)

# --- Create Year Entry Box ---
yearEntry = ttk.Entry(root)
yearEntry.grid(row=0, column=1, columnspan=1, sticky=W)
yearEntry.delete(0, END)
yearEntry.insert(0, '')

# --- Keep Window Open ---
root.mainloop()
