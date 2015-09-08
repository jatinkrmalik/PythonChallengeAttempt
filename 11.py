__author__ = 'Jatin'
from BeautifulSoup import BeautifulSoup
import requests, urllib, os.path as fcheck
from PIL import Image

churl = "http://www.pythonchallenge.com/pc/return/5808.html"
imgurl = "http://www.pythonchallenge.com/pc/return/cave.jpg"
# Looks like 2 images fused in one as Odd even pixels.
username = 'huge'
password = 'file'

if fcheck.isfile("cave.jpg"):
    print("It exists..")

else:
    print("Downloading..")
    response = requests.get(imgurl, auth=(username, password))
    if response.status_code == 200:
        img = open("cave.jpg", "wb")
        img.write(response.content)
        img.close()

chimg = Image.open("cave.jpg")
size = chimg.size
print(size)
pxlst = list(chimg.getdata())
print pxlst[0]
evenlst = pxlst[0::2]
oddlst = pxlst[1::2]
print len(pxlst)
print(len(oddlst))
print(len(evenlst))

oddImg = Image.new("RGB", (640,480), color=0)
oddImg.putdata(evenlst)
oddImg.putdata(oddlst)
oddImg.show()
