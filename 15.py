__author__ = 'jmalik'
import requests, BeautifulSoup, datetime, ospath as fcheck

churl = "http://www.pythonchallenge.com/pc/return/"
param = "cat.html"

response = requests.get(churl+param, auth=("huge","file"))
soup = BeautifulSoup.BeautifulSoup(response.content)
# Let's go to UZI, we will anyway hear from it later
param = soup.find('b').text+".html"

response = requests.get(churl+param, auth=("huge","file"))
soup = BeautifulSoup.BeautifulSoup(response.content)
# print soup.prettify()

for year in range(1996,1582, -20):
    if datetime.date(year,1,1).weekday() == 3:
        print year

# Ahan Youngest would be 1756, a quick Google search tells that 27th jan 1756 was Mozart's bday :D

param= "mozart.html"
print "Go to "+churl+param