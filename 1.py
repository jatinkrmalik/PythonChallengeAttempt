__author__ = 'jmalik'
inputfile = open('./level1', 'r')
inputstring = inputfile.read()
url = "map"
a = ''
# for i in inputstring:
for i in inputstring:
    if ord(i) >= 97 and ord(i) <= 120:
        i = chr(ord(i) + 2)
    elif ord(i) == 121 or ord(i) == 122:
        i = chr(ord(i) - 24)
    a = a[:] + i
print(a)