__author__ = 'jmalik'
from BeautifulSoup import BeautifulSoup
import requests, urllib, os.path as fcheck
from PIL import Image

churl = "http://www.pythonchallenge.com/pc/return/evil.html"
gfxurl = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
username = 'huge'
password = 'file'

if fcheck.isfile("evil2.gfx"):
    print("It exists..")

else:
    print("Downloading..")
    response = requests.get(gfxurl, auth=(username, password))
    if response.status_code == 200:
        gfx = open("evil2.gfx", "wb")
        gfx.write(response.content)
        gfx.close()

# chgfx = open("evil2.gfx", "rb")
# data = chgfx.read()
# chgfx.close()

chgfx = open("evil2.gfx", 'rb').read()
# Splitting the file into 5 dat files.
for i in range(5):
    open("image" + str(i) + ".dat", "wb").write(chgfx[i::5])
#open the image?.dat files with GUI.