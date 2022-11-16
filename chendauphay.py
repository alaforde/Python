s = input()
a = list(map(int, list(s)))
n = len(s)-3
while n > 0:
    a.insert(n, ",")
    n -= 3
for i in a:
    print(i, end = "")
