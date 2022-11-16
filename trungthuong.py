t = int(input())
for v in range(t):
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().strip().split())))
    dict = {}
    maxValue = 0
    key = 1000
    for x in a:
        if x not in dict:
            dict[x] = 1
        else: 
            dict[x] += 1
    for x, y in dict.items():
        if maxValue < y:
            maxValue = y
            key = x
    for x, y in dict.items():
        if maxValue == y and x < key:
            key = x
    print(key)
    
        
           
    