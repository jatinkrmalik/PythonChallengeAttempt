__author__ = 'Jatin'

import requests, urllib2, cookielib,urllib

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
hdnmsg = "" # To store the hidden message
response = opener.open(churl + init_arg).read()
while flag:
    response = opener.open(churl + init_arg)
    html = response.read()
    print html
    for cookie in jar:
        # We know it ends on %90 (hit n trial?)
        if cookie.value=="%90":
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
print "Encoded bz2 string is: ",hdnmsg
import bz2
print "*********************"
print "Drum roll....\n"
print bz2.decompress(urllib.unquote_plus("".join(hdnmsg)))
