# cook your dish here
t = int(input(''))
while(t>0):
    d , l , r = [int(x) for x in input("").split()]
    if (d>=l and d<=r):
        print("Take second dose now")
    elif(d<l):
        print("Too Early")
    else:
        print("Too Late")
    t =t -1