__author__ = 'Jatin'

import requests, urllib2, BeautifulSoup, os.path as fcheck
from PIL import Image

churl = "http://www.pythonchallenge.com/pc/return/balloons.html"

if fcheck.isfile("balloons.jpg"):
    print "Balloons.jpg already exists. \nSkipping download..."

else:
    chimgurl = "http://www.pythonchallenge.com/pc/return/balloons.jpg"
    response = requests.get(chimgurl, auth=("huge", "file"))
    chimg = open("balloons.jpg", "wb")
    chimg.write(response.content)
    chimg.close()

chimg = Image.open("balloons.jpg")
ox, oy = chimg.size
print ox, oy

img1 = Image.new("RGB", (ox / 2, oy), "Red")
# img1.show()
img2 = Image.new("RGB", (ox / 2, oy), "Green")
# img2.show()

# pxlval = open("level18","w")


for _oy in range(0, oy):
    for _ox in range(0, ox):
        if _ox < ox / 2:
            img1.putpixel((_ox, _oy), chimg.getpixel((_ox, _oy)))
        else:
            img2.putpixel((_ox - ox / 2, _oy), chimg.getpixel((_ox, _oy)))

# img1.show()
# img2.show()

r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()

# img1.save("img1.jpg", "JPEG")
# img2.save("img2.jpg", "JPEG")
# nwim1 = Image.merge("RGB",(r1,g2,b1))
# nwim1.show()

diffImg = Image.new("RGB", (ox / 2, oy), "Black")
for _oy in range(0, oy):
    for _ox in range(0, ox / 2):
        r1, g1, b1 = img1.getpixel((_ox, _oy))
        r2, g2, b2 = img2.getpixel((_ox, _oy))
        # print r2 - r1, g2 - g1, b2 - b1
        diffImg.putpixel((_ox, _oy), (r2 - r1, g2 - g1, b2 - b1))

diffImg.show()
