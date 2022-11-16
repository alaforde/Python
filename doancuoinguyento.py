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
    a = input()
    s = int(a[-4:])
    if(prime(s)):
        print("YES")
    else:
        print("NO")