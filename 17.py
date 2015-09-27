__author__ = 'Jatin'

import requests

churl = "http://www.pythonchallenge.com/pc/return/romance.html"

# It's a cookie but I see no cookie in the page. Hmm!

# Let's save the image anyway!

response = requests.get("http://www.pythonchallenge.com/pc/return/cookies.jpg", auth=("huge","file"))

img = open("cookies.jpg", "wb")
img.write(response.content)
img.close()