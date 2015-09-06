import zipfile, urllib, urllib2

zf = urllib.URLopener()
zf.retrieve("http://www.pythonchallenge.com/pc/def/channel.zip","channel.zip")

czip = zipfile.ZipFile("channel.zip","r")
fname = 'readme.txt'
flag = True
it = 0
while flag:
    cnt = 0
    msg = czip.read(fname)
    msgLst = msg.split()
    for el in msgLst:
        if el.isdigit():
            it+=1
            #When you run this you will get that we need comments of the files not the content ;)
            #print it,el
            print czip.getinfo(fname).comment,
            fname= str(el)+".txt"
            cnt+=1
            break
    if cnt==0:
        #print msg
        flag=False