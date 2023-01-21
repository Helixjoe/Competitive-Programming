
def substringGenerator(str):
    start = 0
    sub = []
    lengthOfStr = []
    for k in range(2,len(str)+1):
            if(str[start:k] in x): 
                sub.append(str[start:k]) 
    for el in sub:
        lengthOfStr.append(len(el))
    id = lengthOfStr.index(max(lengthOfStr))
    return sub[id]


t = int(input(''))
while(t>0):
    strings = []
    n = int(input(''))
    for i in range(n):
            s = input('')
            strings.append(s)
    m = int(input(''))
    x = input('')
    truthX= []
    for j in strings:
        truthX.append(substringGenerator(j))
    print(truthX)
    truthXX=[]
    for h in truthX:
        truthXX.append(h)
#this is where we take substrings and check with the target string
    for i in truthX:
        for j in truthX:
            com1 = i + j
            if(com1 in x):
                truthXX.append(com1)
                continue
            com2 = j + i
            if(com2 in x):
                truthXX.append(com2)
    print(truthXX)
    t = t-1