t = int(input())
for i in range(t):
    s = input()
    ok = 1
    for j in range(1000):
        if(int(s)%7 == 0):
            print(s)
            ok = 0
            break
        s = str(int(s) + int(s[::-1]))           
    if ok:
        print("-1")