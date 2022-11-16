t = int(input())
for v in range(t):
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().strip().split())))
    dict = {}
    maxx = 0
    key = 0
    for x in a:
        if x not in dict:
            dict[x] = 1
        else: 
            dict[x] += 1
    for x, y in dict.items():
        if maxx < y:
            maxx = y
            key = x
    if maxx > n/2:
        print(key)
    else:
        print('NO')
        
           
    