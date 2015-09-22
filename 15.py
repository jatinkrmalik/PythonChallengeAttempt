__author__ = 'jmalik'
import requests, BeautifulSoup

churl = "http://www.pythonchallenge.com/pc/return/"
param = "cat.html"

response = requests.get(churl+param, auth=("huge","file"))
soup = BeautifulSoup.BeautifulSoup(response.content)
# Let's go to UZI, we will anyway hear from it later
param = soup.find('b').text+".html"

response = requests.get(churl+param, auth=("huge","file"))
soup = BeautifulSoup.BeautifulSoup(response.content)
print soup.prettify()
