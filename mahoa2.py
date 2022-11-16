p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    q = input()
    q.split()
    if q == '0':    break
    k, s = q.split()
    a = list(s)
    for i in range(len(a)):
        tmp = p.find(a[i])
        a[i] = p[(tmp + int(k))%28]
    a.reverse()
    print(''.join(a))

