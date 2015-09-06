import urllib,re
from PIL import Image

file_URL = "http://www.pythonchallenge.com/pc/def/oxygen.png"
download = urllib.urlopen(file_URL)
img = download.read()
savedFile = open("oxygen.png", 'wb')
savedFile.write(img)
savedFile.close()

chimg = Image.open("oxygen.png")
x,y=chimg.size
print "Width:",x,"Height:",y
grlst = []
nwlst = []
for w in range(0,x,7):
    grlst.append(chimg.getpixel((w,y/2)))

for el in grlst:
    if el[0]==el[1]==el[2]:
        nwlst.append(el[0])
final = ""
print "The new list is",nwlst
for num in nwlst:     
        final+=chr(int(num))
print final

#print "".join(map(chr,re.findall('(\[)(\d*, )*(\d*])',final)))
print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
