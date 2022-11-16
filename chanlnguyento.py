import math

def prime(n):
    i = 5
    if n < 2: 
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        while i*i < n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6
        return True
    
t = int(input())
for v in range(t):
    check = True
    s = input()
    sum = 0
    for i in range(len(s)):
        k = int(s[i])
        sum += k
        if (k^i) % 2 != 0:
            check = False
            break
    if(not prime(sum)):
        check = False
    if(check):
        print("YES")
    else:
        print("NO")
        
