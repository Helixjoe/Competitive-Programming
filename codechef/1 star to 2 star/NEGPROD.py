t = int(input(''))
while(t>0):
    a , b , c = [int(x) for x in input("").split()]
    if(a<0):
        if(b<=0 and c<=0):
            print("NO")
        else:
            print("YES")
    elif(b<0):
        if(a<=0 and c<=0):
            print("NO")
        else:
            print("YES")
    elif(c<0):
        if(a<=0 and b<=0):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
    t = t-1