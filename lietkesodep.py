t = int(input())
for v in range(t):
    s = input()
    k = s[0:len(s)//2+1]
    n = int(s)
    m = int(k)
    i = 0
    while i < m:
        i += 2 
        s1 = str(i)
        tmp = s1 + s1[::-1]
        check = 0
        if(int(tmp) > n): break
        for j in s1:
           if(int(j)%2 != 0):
               check = 1 
        if(check == 0):    
            print(tmp, end = ' ')
    print()
    
    