t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    for i in a:
        k ^= i
    print(k)
