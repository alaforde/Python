t = int(input())
for v in range(t):
    s = input()
    ok = True
    if s[0] == s[1]:
        ok = False 
    for i in range(len(s)-3):
        if s[i] != s[i+2] or s[i+1] != s[i+3]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")