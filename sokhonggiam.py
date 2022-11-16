t = int(input())
for i in range(t):
    s = input()
    check = 1
    for j in range(len(s)-1):
        if(s[j] > s[j+1]):
            check = 0
            break
    if(check):
        print("YES")
    else:
        print("NO")