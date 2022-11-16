from operator import truediv


t = int(input())
for v in range(t):
    s = input()
    check = True
    if(len(s)%2 == 0):
        check = False
    else:
        if s[1] == s[0]:    
            check = False
        else:
            for i in range(0, len(s)-2, 2):
                if s[i] != s[i+2]:
                    check = False   
                else: 
                    break
    if(check):
        print("YES")
    else:
        print("NO")