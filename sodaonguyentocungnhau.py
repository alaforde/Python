import math
t = int(input())
for v in range(t):
    s = input()
    d = s[::-1]
    if(math.gcd(int(s), int(d)) == 1):
        print("YES")
    else:
        print("NO")