__author__ = 'jmalik'

import urllib, requests, os.path as fcheck
from PIL import Image
from pprint import pprint

churl = "http://www.pythonchallenge.com/pc/return/italy.html"

if fcheck.isfile("wire.png"):
    print("It exists..")

else:
    getImg = requests.get("http://www.pythonchallenge.com/pc/return/wire.png", auth=("huge","file"))
    fi = open("wire.png", "wb")
    fi.write(getImg.content)
    fi.close()


chImg = Image.open("wire.png")

pxlst = list(chImg.getdata())

newImg = Image.new("RGB", (100,100), "white")

newImg.putdata(pxlst)
newImg.show()
