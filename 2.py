__author__ = 'jmalik'
inputfile = open('./level2', 'r')
inputstring = inputfile.read()
# 
# for alpha in inputstring:
#     cnt = inputstring.count(alpha)
#     if cnt <=1:
#         print(alpha, ":", cnt)
# 
output = ""  # empty string
counts = {}
for c in inputstring:
    if c in counts.keys():
        continue
    counts[c] = inputstring.count(c)
    if counts[c] < 100:  # guess that rare characters will occur less than 100 times
        output += c

print(output)
