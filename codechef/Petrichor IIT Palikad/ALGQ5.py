def flip(str,cond,start,stop):
    new = str[0:start] + cond + str[stop:len(str)]
    return new


t = int(input(''))
while(t>0):

    c = 0
    flag = 1
    n , k  = [int(x) for x in input("").split()]
    a = input('')
    b = input('')
    start = 'b'
    for i in range(k):
        sub = ""
        if(a[i]==b[i]):
            flag = 1
        else:
            start = i
            flag = 0
            sub += a[i]
        if(flag == 1 and start!='b'):
            stop = i
            b = flip(b,sub,start,stop)
            c = c+1
            continue
        if(k>c):
            print(b)
            print("NO")
            flag = 0
            break
    if(c==k and flag == 1):
        print("YES")
    t = t -1