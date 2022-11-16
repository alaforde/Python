t = int(input())
for i in range(t):
    a = input()
    s = list(map(int,list(a)))
    n = len(s)-1
    remember = 0
    while n >= 1:
        if(s[n] >= 5):
            remember = 1  
        s[n] = 0   
        n -= 1
        if(remember): 
            s[n] += 1
            remember = 0
    if(remember):
        print("1", end = "")
    for i in s:
        print(i, end = "")
    print("")