churl = "http://www.pythonchallenge.com/pc/return/bull.html"

dd = {1:"ONE", 2:"TWO", 3:"THREE"}
ddrev = {"ONE":1,"TWO":2,"THREE":3}
init = 1

def countDigit(num):
    count = 0
    for _ in str(num):
        count +=1

    return count
print init
ans = countDigit(init)
init = int(str(ddrev[dd[ans]])+str(ddrev[dd[init]]))
print init
ans = countDigit(init)
print int(str(ddrev[dd[ans]])+str(ddrev[dd[1]]))