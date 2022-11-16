a = []
b = [0]*42
cnt = 0
while len(a) < 10:
    a.extend(list(map(int, input().split())))
for x in a:
    b[x%42] += 1
for x in b:
    if x != 0:
        cnt += 1
print(cnt)