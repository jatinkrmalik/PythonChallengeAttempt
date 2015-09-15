import urllib

# Phone the devil
churl = "http://www.pythonchallenge.com/pc/return/disproportional.html"
pbook = "http://www.pythonchallenge.com/pc/phonebook.php"

# Something to do with a call to php file
response = urllib.urlopen(pbook).read()
print response

