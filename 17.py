__author__ = 'Jatin'

import requests, urllib2, cookielib

churl = "http://www.pythonchallenge.com/pc/return/romance.html"

# It's a cookie but I see no cookie in the page. Hmm!
# There is a cookie dumbhead

# Let's save the image anyway!
# response = requests.get("http://www.pythonchallenge.com/pc/return/cookies.jpg", auth=("huge","file"))
#
# img = open("cookies.jpg", "wb")
# img.write(response.content)
# img.close()

# Cookie says you should have follow busynothing! Taking learnings from Level 4.

churl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
init_arg = "65071"

# flag = True
# response = ""
# response = urllib2.urlopen(churl + init_arg)
# while flag:
#     response = urllib2.urlopen(churl + init_arg)
#     html = response.read()
#     print html
#     print "----------------------------------------"
#     lst = html.split()
#     intCount = 0
#     el = lst[-1]
#     print el
#     init_arg=el
#     intCount+=1
#
#     if intCount==0:
#         print html
#         ch=raw_input("Is it the end?")
#         if ch=="no" or "n":
#             init_arg=str(int(init_arg)/2)
#         else:
#             print("Go to"+str(html))
#
# # Struck in a loop :(

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(jar)
opener = urllib2.build_opener(auth_handler, cookie_handler)
opener.open('http://www.pythonchallenge.com/pc/return/romance.html')
print list(jar)

print opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345').read()
print list(jar )