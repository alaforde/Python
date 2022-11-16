t = int(input())
for v in range(t):
    s = input()
    check = 1
    sum = int(s[-1])
    for i in range(len(s)-1):
        sum += int(s[i])
        if int(s[i]) - int(s[i+1]) != 2 and int(s[i+1]) - int(s[i]) != 2:
            check = 0
            break
    if(sum%10 == 0 and check):
        print("YES")
    else:
        print("NO") 