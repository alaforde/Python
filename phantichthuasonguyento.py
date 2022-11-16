t = int(input())
for i in range(t):
    n = int(input())
    print("1", end = " ")
    i = 3
    k = 0
    while n%2 == 0:
        n /= 2
        k += 1
    if(k != 0):
        print(f'* 2^{k} ', end = '')
    while n != 1:
        cnt = 0
        while n%i == 0:
            n /= i
            cnt += 1
        if(cnt != 0):
            print(f'* {i}^{cnt} ', end = '')
        i += 2
    print()