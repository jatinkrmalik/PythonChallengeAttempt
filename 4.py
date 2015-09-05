__author__ = 'Jatin'
import urllib2;

churl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
init_arg = "9401"
flag = True 
response = ""
while flag:
    response = urllib2.urlopen(churl + init_arg)
    html = response.read()
    lst = html.split()
    intCount = 0
    for el in lst:
        if el.isdigit():
            print el
            init_arg=el
            intCount+=1
            
    if intCount==0:
        print html
        raw_input("Is it the end?")
        init_arg=str(int(init_arg)/2)

