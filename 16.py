__author__ = 'jmalik'
import requests, BeautifulSoup
from PIL import Image

churl = "http://www.pythonchallenge.com/pc/return/"
param = "mozart.html"

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