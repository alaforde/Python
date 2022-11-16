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
    cnt = 0
    if prime(len(s)) == False:
        ok = False
    for i in s:
        if i == '2' or i == '3' or i == '5' or i == '7':
            cnt += 1
    if cnt < len(s)//2:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")