import urllib2
import pickle

churl="http://www.pythonchallenge.com/pc/def/"
arg="peak.html"
response = urllib2.urlopen(churl+arg)
html = response.readlines()

for line in html:
    if "<peakhell" in line:
        print line

#Now we know about banner.p
response = urllib2.urlopen(churl+"banner.p")
html = response.read()
#print "Let us see what's in Banner.p\n\n",html

print "Peak hell == pickle? Let's save it all in a file"
peakFile = open("./level5","w")
peakFile.write(html)
peakFile.close()

peakFile = open("./level5","r")
mysteryText = pickle.load(peakFile)
total = ""
for lst in mysteryText:
    for el in lst:
       total+=el[0]*int(el[1])
print total


