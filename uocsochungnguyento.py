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

def sum(n):
    tmp = 0
    while n > 0: 
        tmp += n%10
        n //= 10
    return tmp
t = int(input())
for v in range(t):
    a, b = map(int, input().split())
    k = math.gcd(a, b)
    if prime(sum(k)): 
        print("YES")
    else:
        print("NO") 