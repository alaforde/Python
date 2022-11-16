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
    s = input()
    ok = True
    if(prime(int(s)) == False) or (prime(int(s[::-1])) == False):
        ok = False
    for i in s:
        if i != '2' and i != '3' and i != '7' and i != '5':
            ok = False
            break
    if ok:
        print('Yes')
    else:
        print('No')