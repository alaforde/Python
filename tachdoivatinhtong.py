s = input()
while int(s) > 10:
    n = len(s)//2
    s = str((int)(s[0:n])+ (int)(s[n:]))
    print(s)