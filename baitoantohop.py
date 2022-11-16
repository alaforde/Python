from itertools import combinations, permutations

n, k = map(int, input().split())
a = []
s = set()
while len(a) < n:
    a.extend(list(map(int, input().strip().split())))
for x in a:
    s.add(x)  
s = sorted(list(s))
if(k < len(s)):
    k = combinations(s, k)
    for x in k:
        print(*x)