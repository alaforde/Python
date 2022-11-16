import re
t = int(input())
a = []
for _ in range(t):
    s = input()
    m = re.findall(r'\d+', s)
    for i in m:
        a.append((int)(i))
a.sort()
for x in a:
    print(x)