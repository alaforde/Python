t = int(input())
for v in range(t):
    s = input()
    i = 0
    while i < len(s):
        j = i
        cnt = 0
        while j < len(s) and s[i] == s[j]:
            j += 1
            cnt += 1
        print(f'{cnt}{s[i]}', end = "")
        i = j
    print()