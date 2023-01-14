# cook your dish here
t = int(input(''))
while(t>0):
    a , b , x = [int(x) for x in input("").split()]
    y = (b-a)/x
    print(int(y))
    t = t-1
