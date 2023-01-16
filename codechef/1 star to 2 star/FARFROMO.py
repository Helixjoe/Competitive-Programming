t = int(input(''))
while(t>0):
    x1, y1, x2, y2 = [int(x) for x in input("").split()]
    d1 = math.sqrt(x1**2 + y1**2)
    d2 = math.sqrt(x2**2 + y2**2)
    if(d1>d2):
        print("ALEX")
    elif(d2>d1):
        print("BOB")
    else
        print("EQUAL")
    t=t-1