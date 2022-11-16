t = int(input())
for v in range(t):
    s = input()
    idx = 0
    ok = True
    if(len(s) < 3):
        ok = False
    for i in range(1,len(s)):
        if(s[i] <= s[i-1]):
            idx = i - 1
            break
    if(idx == 0):
        idx = len(s) - 1
    for i in range(idx, len(s)-1):
        if(s[i+1] >= s[i]):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")