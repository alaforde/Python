while True:
    n = int(input())
    if n == 0:
        break
    s = set()
    s.add(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
            s.add(n)
        else:
            n = n*3 + 1
            s.add(n)
    print(len(s))