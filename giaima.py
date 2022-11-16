t = int(input())
for v in range(t):
    s = input()
    for i in range(len(s)):
        if s[i].isdigit():
            k = int(s[i])
            for j in range(k):
                print(s[i-1], end = "")
    print("")