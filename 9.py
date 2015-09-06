import urllib
from PIL import Image

file_URL = "http://www.pythonchallenge.com/pc/return/good.jpg"
download = urllib.urlopen(file_URL)
img = download.read()
savedFile = open("good.jpg", 'wb')
savedFile.write(img)
savedFile.close()

chimg = Image.open("good.jpg")
print chimg.size
