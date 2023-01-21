t = int(input(''))
while(t>0):
    req = ['e','a','s','y']
    s = input('')
    for i in s:
        if i in req:
            req.remove(i)
    if req == []:
        print("YES")
    else:
        print("NO")    
    t = t -1