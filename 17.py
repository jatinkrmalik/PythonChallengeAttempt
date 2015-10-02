__author__ = 'Jatin'

import requests, urllib2, cookielib, urllib

churl = "http://www.pythonchallenge.com/pc/return/romance.html"

# It's a cookie but I see no cookie in the page. Hmm!
# There is a cookie dumb head, check in chrome dev console

# Cookie says you should have follow busynothing! Taking learnings from Level 4. Clever!
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(auth_handler, cookie_handler)
opener.open('http://www.pythonchallenge.com/pc/return/romance.html')
print list(jar)

churl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
init_arg = "12345"

opener.open(churl + init_arg)
print list(jar)

print "\nAhan! there is a hidden message in the cookie. Look in value above^"
print "\nLet us loop in the busynothing and store the value in a string"
flag = True
hdnmsg = ""  # To store the hidden message
response = opener.open(churl + init_arg).read()
while flag:
    response = opener.open(churl + init_arg)
    html = response.read()
    print html
    for cookie in jar:
        # We know it ends on %90 (hit n trial?)
        if cookie.value == "%90":
            hdnmsg += cookie.value
            flag = False
        else:
            hdnmsg += cookie.value
    print "String is", hdnmsg
    print "----------------------------------------"
    lst = html.split()
    intCount = 0
    el = lst[-1]
    print el
    init_arg = el

print "*********************"
print "Encoded bz2 string is: ", hdnmsg
import bz2

print "*********************"
print "Drum roll....\n"
print bz2.decompress(urllib.unquote_plus("".join(hdnmsg)))

# Oh wait! It's not over yet. The output says "is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand."
# This is a reference to level 15 where 27th Jan was bday of Wolfgang Amadeus Mozart and message says to *call* his father.
# Call is a reference to level 13. I think we should attempt a call to Leopold Mozart (father of Wolfgang Amadeus Mozart). Man this is inceptional

# Taking cues from 13.py
import xmlrpclib
churl = "http://www.pythonchallenge.com/pc/return/disproportional.html"
pbook = "http://www.pythonchallenge.com/pc/phonebook.php"
phonebook = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(phonebook.system.listMethods())
print phonebook.system.methodHelp('phone')
print phonebook.system.methodSignature('phone')

print phonebook.phone("Leopold")
# returns 555-VIOLIN

# Hitting http://www.pythonchallenge.com/pc/return/violin.html return "no! i mean yes! but ../stuff/violin.php."