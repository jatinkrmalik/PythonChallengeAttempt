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

spiralImg = Image.new(chImg.mode, (100,100), 0)
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
x,y,z = -1,0,0
for i in range(200):
    d = dirs[i % 4]
    for j in range(100 - (i + 1) // 2):
        x += d[0]
        y += d[1]
        spiralImg.putpixel((x,y), chImg.getpixel((z,0)))
        z += 1

# WTF! It's a CAT :D
spiralImg.show()
