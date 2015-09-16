import urllib
import xmlrpclib
import pprint


# Phone the devil
churl = "http://www.pythonchallenge.com/pc/return/disproportional.html"
pbook = "http://www.pythonchallenge.com/pc/phonebook.php"

# Something to do with a call to php file
# response = urllib.urlopen(pbook).read()
# print response

# We will now use XML-RPC
phonebook = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(phonebook.system.listMethods())