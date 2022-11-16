t = int(input())
for v in range(t):
    s = input()
    a = []
    for i in range(len(s)):
        if s[i].isdigit() and (i == 0 or s[i-1].isdigit() == 0):
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            a.append(int(s[i:j]))
    print(min(a))