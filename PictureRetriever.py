''' tk_ImageTest_url.py
display an image from a URL using Tkinter, PIL and io
PIL allows the use of image formats other than gif
tested with Python27 and Python34  by  vegaseat (dns)  10mar2015
'''
import io
from PIL import Image, ImageTk
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
root = tk.Tk()
root.title("Show image from URL")
# find yourself a picture on an internet web page you like
# (right click on the picture and copy the image URL)
#pic_url = "http://www.google.com/intl/en/images/logo.gif"
# split a long url
# url1 = "https://beccaboosandkimblebees.files.wordpress.com/"
# url2 = "2013/02/tumblr_mhm8uaxf731rrufwao1_500_large.jpg"
# pic_url = url1 + url2

pic_url = 'https://images-na.ssl-images-amazon.com/images/I/518aPA5ybOL._SY400_.jpg'
# open the web page picture and read it into a memory stream
# and convert to an image Tkinter can handle
my_page = urlopen(pic_url)
# create an image file object
my_picture = io.BytesIO(my_page.read())
# use PIL to open image formats like .jpg  .png  .gif  etc.
pil_img = Image.open(my_picture)
# convert to an image Tkinter can use
tk_img = ImageTk.PhotoImage(pil_img)
# put the image on a typical widget
label = tk.Label(root, image=tk_img)
label.pack(padx=5, pady=5)
root.mainloop()