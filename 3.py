from collections import Counter
import re
# import urllib.request
# import bs4
# from bs4 import BeautifulSoup
#
# churl = "http://www.pythonchallenge.com/pc/def/equality.html"
# full = urllib.request.urlopen(churl)
#
# src = BeautifulSoup(full.read(),"html.parser")
# srcStr = str(src)
# comments = re.finditer( "<!--[^>]*-->",srcStr)
# print(comments)

#make sure to consider "EXACTLY" 3 Bodyguards
pattern = re.compile("([^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z])")
testFile = open("./level3", "r")
lines = testFile.readlines()
lst = []
for line in lines:
    for match in re.finditer(pattern,line):
        lst.append(match.group())

print(lst)

for el in lst:
    print(el[4], end="")



