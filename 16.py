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
print chImg.size
# x = Image(a)

lst = list(chImg.getdata())

pxlval = open("pxl.txt", "wb")
pxlval.write(str(lst))

arr = 640*480

chImgNew = Image.new("RGB", (int(arr),1), "Black")
chImgNew.show()
