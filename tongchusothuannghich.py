t = int(input())
for v in range(t):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if sum < 10:
        print("NO")
    else:
        a = str(sum)
        b = a[::-1]
        if a == b:
            print("YES")
        else:
            print("NO") 