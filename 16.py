__author__ = 'jmalik'
import requests, BeautifulSoup
from PIL import Image
import os.path as fcheck
churl = "http://www.pythonchallenge.com/pc/return/"
param = "mozart.html"

if fcheck.isfile("mozart.gif"):
    print "It exists.."

else:
    response = requests.get(churl+param, auth=("huge","file"))

    soup = BeautifulSoup.BeautifulSoup(response.content)
    print soup.find("img")

    imgResponse = requests.get(churl+"mozart.gif", auth=("huge","file"))

    chImg = open("mozart.gif","wb")
    chImg.write(imgResponse.content)
    chImg.close()

chImg = Image.open("mozart.gif")
w,h = chImg.size
print w,h
# x = Image(a)

bars = []
magenta = 195   # deduced by looking at the GIF's colour palette in GraphicConverter
for j in range(h):
    for i in range(w - 5):
        if chImg.getpixel((i,j)) == magenta and chImg.getpixel((i+4,j)) == magenta:
            bars.append((i,j))

print bars
#One magenta bar per line.