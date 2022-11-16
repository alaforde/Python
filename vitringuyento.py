def check(s, b):
    for i in range(len(s)):
        if (b.count(i) == 1 and b.count(int(s[i])) == 0) or (b.count(i) == 0 and b.count(int(s[i])) == 1):
            return 'NO'
    return 'YES'


a = [True]*(501)
b = []
a[0] = a[1] = False
for i in range(2, 501):
    if a[i] == True:
        b.append(i)
        j = 2*i
        while j < 501:
            a[j] = False
            j = j+i
t = int(input())
for i in range(t):
    s = input()
    print(check(s, b))
