churl = "http://www.pythonchallenge.com/pc/return/bull.html"

# Storing the first element i.e 1 in a list.
lst = [1]

# Well challenge asks for len(a[30]) so iterating the algo 30 times.
for _ in range(30):

    # This will store end result of every iteration before passing itself in the loop
    templst = []
    i = 0
    while i < len(lst):
        a = lst[i]
        count = 1
        if i < len(lst) - 1:
            b = lst[i + 1]
            if a == b:
                count += 1
                if i < len(lst) - 2:
                    c = lst[i + 2]
                    if b == c:
                        count += 1
                        templst.extend([count, c])
                        i += 3
                    else:
                        templst.extend([count, b])
                        i += 2
                else:
                    templst.extend([count, b])
                    i += 2
            else:
                templst.extend([count, a])
                i += 1
        else:
            templst.extend([count, a])
            i += 1
    lst = templst

print "Do you dare. Here you go: \n",("".join(str(x) for x in lst)) # Just for fun
print "\nLength of a[30] is:", len(lst) # Fin.
