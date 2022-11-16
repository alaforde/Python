t = int(input())
for v in range(t):
    s = input()
    s += "0"
    sum = 0
    mul = 1
    check = True
    for i in range(0, len(s)-1, 2):
        sum += int(s[i+1])
        if s[i] != '0':
            mul *= int(s[i])
            check = False
    if(check):
        mul = 0
    print(mul, sum)