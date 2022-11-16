n = int(input())
a = [float(i) for i in input().split()]
s = sum(a)
for x in a:
    if x == min(a):
        s -= min(a)
        n -= 1
    elif x == max(a):
        s -= max(a)
        n -= 1
print(format(s/n, '.2f'))