# cook your dish here
t = int(input(''))
while(t>0):
    x = int(input(''))
    if(x<=70):
        print(0)
    elif(x>70 and x<=100):
        print(500)
    elif(x>100):
        print(2000)
    t = t-1