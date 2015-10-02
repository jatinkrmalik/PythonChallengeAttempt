__author__ = 'Jatin'

import requests, urllib2, BeautifulSoup
from PIL import Image

churl = "http://www.pythonchallenge.com/pc/return/balloons.html"

respose = requests.get(churl, auth=("huge","file"))
print respose.content

chimg = Image.open("http://www.pythonchallenge.com/pc/return/balloons.jpg")
print Image.size
