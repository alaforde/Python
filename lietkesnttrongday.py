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
    
n = int(input())
a = []
while(len(a) < n):
    a.extend(list(map(int, input().split())))
dict = {}
for i in a:
    if prime(i):
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
for x, y in dict.items():
    print(x, y)